import os
import json
import subprocess
from pathlib import Path
from manimator.utils.visual_analyzer import VisualLayoutAnalyzer
from manimator.utils.dual_model_config import DualModelConfig
from dotenv import load_dotenv

load_dotenv()

SCENE_FILE = Path("scene_d29f69ad-efc3-48a9-862a-ff47b882d2c7.py")
SCENE_NAME = "MultivariableCalculusExplanation"
VIDEO_PATH = Path("media/videos/scene_d29f69ad-efc3-48a9-862a-ff47b882d2c7/1080p60/MultivariableCalculusExplanation.mp4")

def render_scene(disable_caching: bool = False) -> str:
    print(f"🎬 Rendering {SCENE_NAME} in 1080p...")
    # Use -pqh for high quality 1080p60
    # Capture output to parse partial movie files
    # --progress_bar none to avoid log pollution
    cmd = ["manim", "-pqh", "--progress_bar", "none", str(SCENE_FILE), SCENE_NAME] 
    
    if disable_caching:
        print("  - ⚠️ Caching disabled (forcing full re-render)...")
        cmd.insert(2, "--disable_caching")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Rendering failed:\n{result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, cmd, result.stdout, result.stderr)
        
    print("✅ Rendering complete.")
    return result.stderr + "\n" + result.stdout

def extract_ordered_partial_files(render_output: str, partial_dir: Path) -> list[Path]:
    """
    Parse Manim output to find the sequence of partial movie files.
    """
    import re
    
    # Strip ANSI codes
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    clean_output = ansi_escape.sub('', render_output)
    
    ordered_files = []
    lines = clean_output.splitlines()
    
    # Strategy: The log contains hashes in the format `\d+_\d+_\d+`.
    # These appear sequentially for each animation, either in "Using cached data" or "written in ...".
    # We extract all such patterns and verify they exist as files.
    
    hash_pattern = re.compile(r"(\d+_\d+_\d+)")
    all_hashes = hash_pattern.findall(clean_output)
    
    print(f"  - Found {len(all_hashes)} animation events in log.")
    
    missing_files = []
    for h in all_hashes:
        # Construct path
        file_path = partial_dir / f"{h}.mp4"
        
        # Check primary directory
        if file_path.exists():
            ordered_files.append(file_path)
            continue
            
        # Check alternate directory (handle naming mismatch)
        alt_dir = partial_dir.parent / "MultivariateCalculusExplanation"
        alt_path = alt_dir / f"{h}.mp4"
        
        if alt_path.exists():
            ordered_files.append(alt_path)
            continue
            
        # If missing in both
        missing_files.append(h)

    if missing_files:
        print(f"❌ Critical Error: Missing {len(missing_files)} partial movie files.")
        # Raise error to trigger auto-recovery
        raise FileNotFoundError(f"Missing {len(missing_files)} partial movie files.")

    print(f"✅ Verified existence of all {len(ordered_files)} frames.")
    return ordered_files

def fix_layout():
    print(f"DEBUG: SCENE_NAME = {SCENE_NAME}")
    print(f"DEBUG: VIDEO_PATH = {VIDEO_PATH}")
    partial_dir_check = VIDEO_PATH.parent / "partial_movie_files" / SCENE_NAME
    print(f"DEBUG: partial_dir = {partial_dir_check}")
    print(f"DEBUG: partial_dir exists? {partial_dir_check.exists()}")
    
    analyzer = VisualLayoutAnalyzer(model=DualModelConfig.get_visual_model())
    max_iterations = 5
    
    for i in range(max_iterations):
        print(f"\n🔄 Iteration {i+1}/{max_iterations}")
        
        # 1. Render and Capture Log
        try:
            render_log = render_scene()
        except subprocess.CalledProcessError:
            return

        if not VIDEO_PATH.exists():
            print(f"❌ Video not found at {VIDEO_PATH}")
            return

        # 2. Analyze
        print("🔍 Analyzing layout...")
        
        # Construct path to partial movie files
        partial_dir = VIDEO_PATH.parent / "partial_movie_files" / SCENE_NAME
        
        frame_paths = []
        if partial_dir.exists():
            print("  - Parsing render log for ordered event segments...")
            try:
                video_files = extract_ordered_partial_files(render_log, partial_dir)
            except FileNotFoundError:
                print("⚠️ Missing partial files detected. Triggering forced full re-render...")
                try:
                    render_log = render_scene(disable_caching=True)
                    video_files = extract_ordered_partial_files(render_log, partial_dir)
                except Exception as e:
                    print(f"❌ Auto-recovery failed: {e}")
                    return
            
            if video_files:
                print(f"  - Found {len(video_files)} animation steps in log.")
                print("  - Extracting frames from these steps...")
                # We need a new method in analyzer to extract from a list of files
                frame_paths = analyzer.extract_frames_from_videos(video_files)
                print(f"  - Extracted {len(frame_paths)} frames (one per step).")
            else:
                print("⚠️ Could not parse video files from log. Falling back to directory listing.")
                frame_paths = analyzer.extract_event_frames(partial_dir)
        
        if not frame_paths:
             print(f"⚠️ Partial movie files not found or empty. Falling back to time-based sampling.")
             frame_paths = analyzer.extract_frames(VIDEO_PATH, num_frames=20)
             print(f"  - Extracted {len(frame_paths)} frames (time-based).")
        
        print("  - Analyzing frames...")
        analysis = analyzer.analyze_frames(frame_paths)
        
        # Clean up frames
        for frame in frame_paths:
            frame.unlink()
            
        print(f"  - Analysis result: {json.dumps(analysis, indent=2)}")
        
        if not analysis.get("has_issues", False):
            print(f"✅ No layout issues detected! Quality: {analysis.get('overall_quality')}")
            break
        
        # 3. Fix
        print("⚠️ Issues detected. Generating fixes...")
        with open(SCENE_FILE, "r") as f:
            current_code = f.read()
            
        fixed_code, changes = analyzer.suggest_fixes(analysis, current_code)
        
        if not changes or fixed_code == current_code:
            print("ℹ️  No automatic fixes available for detected issues or code unchanged.")
            break
            
        # Save fixed code
        output_file = SCENE_FILE.with_name(f"{SCENE_FILE.stem}_fixed.py")
        with open(output_file, "w") as f:
            f.write(fixed_code)
        print(f"💾 Fixed code saved to {output_file}")
        
        # Rename original to backup (if not exists or overwrite) and fixed to original
        backup_file = SCENE_FILE.with_name(f"{SCENE_FILE.stem}_backup_{i}.py")
        # Keep the very first backup safe if needed, but here we just backup current state
        if SCENE_FILE.exists():
            import shutil
            shutil.copy(SCENE_FILE, backup_file)
            
        os.rename(output_file, SCENE_FILE)
        print(f"🔄 Updated {SCENE_FILE} with fixes. Backup at {backup_file}")
        
    print("\n🏁 Layout fix process finished.")

if __name__ == "__main__":
    fix_layout()

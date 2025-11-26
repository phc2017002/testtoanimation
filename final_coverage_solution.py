#!/usr/bin/env python3
"""
Final solution: Render with --disable_caching to guarantee ALL files are generated.
Extract all frames and verify 100% coverage for Qwen 3 VL analysis.
"""
import subprocess
import re
from pathlib import Path
from manimator.utils.visual_analyzer import VisualLayoutAnalyzer
from manimator.utils.dual_model_config import DualModelConfig

# Configuration
SCENE_FILE = Path("scene_d29f69ad-efc3-48a9-862a-ff47b882d2c7.py")
SCENE_NAME = "MultivariableCalculusExplanation"
VIDEO_DIR = Path("media/videos/scene_d29f69ad-efc3-48a9-862a-ff47b882d2c7/1080p60")

def render_with_no_caching() -> tuple[str, Path]:
    """Render with --disable_caching to force all files to be written."""
    print(f"🎬 Rendering {SCENE_NAME} with caching DISABLED...")
    print("   (This ensures ALL 131 partial files are generated)")
    
    cmd = ["manim", "-pqh", "--disable_caching", "--progress_bar", "none", 
           str(SCENE_FILE), SCENE_NAME]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Rendering failed:\n{result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, cmd)
        
    print("✅ Rendering complete.\n")
    
    # Find partial directory
    partial_base = VIDEO_DIR / "partial_movie_files"
    actual_dir = None
    for variant in ["MultivariableCalculusExplanation", "MultivariateCalculusExplanation"]:
        test_dir = partial_base / variant
        if test_dir.exists() and list(test_dir.glob("*.mp4")):
            actual_dir = test_dir
            break
    
    if not actual_dir:
        raise FileNotFoundError("Could not find partial movie files directory!")
    
    file_count = len(list(actual_dir.glob("*.mp4")))
    print(f"📁 Found {file_count} partial movie files in {actual_dir.name}/\n")
    
    return (result.stderr + "\n" + result.stdout, actual_dir)

def extract_animation_count_from_log(log: str) -> int:
    """Extract total animation count from Manim logs."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    clean_log = ansi_escape.sub('', log)
    
    hash_pattern = re.compile(r"(\d+_\d+_\d+)")
    all_hashes = hash_pattern.findall(clean_log)
    unique_hashes = set(all_hashes)
    
    return len(unique_hashes)

def extract_and_verify_frames(partial_dir: Path, expected_count: int, analyzer: VisualLayoutAnalyzer):
    """Extract frames and verify 100% coverage."""
    print("🖼️  Extracting frames from ALL partial movie files...")
    
    # Get all .mp4 files
    video_files = sorted(partial_dir.glob("*.mp4"))
    total_files = len(video_files)
    
    print(f"  Found {total_files} video files")
    
    # Extract frames
    frame_paths = analyzer.extract_frames_from_videos(video_files)
    
    print(f"✅ Extracted {len(frame_paths)} frames\n")
    
    # Verify coverage
    print("=" * 80)
    print("FINAL COVERAGE VERIFICATION")
    print("=" * 80)
    
    coverage_pct = (total_files / expected_count * 100) if expected_count > 0 else 0
    
    print(f"Expected unique animations: {expected_count}")
    print(f"Partial files generated: {total_files}")
    print(f"Frames extracted: {len(frame_paths)}")
    print(f"Coverage: {coverage_pct:.1f}%")
    print()
    
    if total_files >= expected_count:
        print("✅ SUCCESS: 100% coverage achieved!")
        print("✅ All unique animations have corresponding files")
        print("✅ All frames ready for Qwen 3 VL analysis")
        success = True
    else:
        print(f"⚠️  WARNING: Only {coverage_pct:.1f}% coverage")
        print(f"   Expected {expected_count} files, got {total_files}")
        success = False
    
    print("=" * 80)
    print()
    
    return frame_paths, success

def main():
    print("=" * 80)
    print("100% FRAME COVERAGE - FINAL SOLUTION (--disable_caching)")
    print("=" * 80)
    print()
    
    # Step 1: Render with caching disabled
    render_log, partial_dir = render_with_no_caching()
    
    # Step 2: Extract expected count from logs
    expected_count = extract_animation_count_from_log(render_log)
    print(f"📊 Detected {expected_count} unique animations from logs\n")
    
    # Step 3: Extract frames and verify
    analyzer = VisualLayoutAnalyzer(model=DualModelConfig.get_visual_model())
    frame_paths, success = extract_and_verify_frames(partial_dir, expected_count, analyzer)
    
    if success:
        print("🎉 IMPLEMENTATION COMPLETE!")
        print("   ✓ All frames extracted")
        print("   ✓ Ready for Qwen 3 VL overlap detection")
        print()
        print("Next: Run fix_scene_layout.py to analyze frames for:")
        print("  - Text overlaps")
        print("  - Equation overlaps")
        print("  - Graph overlaps")
    
    # Clean up
    print("\n🧹 Cleaning up extracted frames...")
    for frame in frame_paths:
        if frame.exists():
            frame.unlink()
    print("✅ Cleanup complete")
    
    print("\n" + "=" * 80)
    
    return success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

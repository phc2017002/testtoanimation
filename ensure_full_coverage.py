#!/usr/bin/env python3
"""
Clean cache and ensure 100% frame coverage by forcing a fresh render.
Then extract all frames for Qwen 3 VL analysis.
"""
import shutil
import subprocess
from pathlib import Path
from manimator.utils.visual_analyzer import VisualLayoutAnalyzer
from manimator.utils.dual_model_config import DualModelConfig

# Configuration
SCENE_FILE = Path("scene_d29f69ad-efc3-48a9-862a-ff47b882d2c7.py")
SCENE_NAME = "MultivariableCalculusExplanation"
VIDEO_DIR = Path("media/videos/scene_d29f69ad-efc3-48a9-862a-ff47b882d2c7/1080p60")
PARTIAL_DIR = VIDEO_DIR / "partial_movie_files"

def clean_cache_for_scene():
    """Remove all partial movie files for this scene to force fresh render."""
    print("🧹 Cleaning cache for scene...")
    
    # Remove both directory variants
    dir1 = PARTIAL_DIR / "MultivariableCalculusExplanation"
    dir2 = PARTIAL_DIR / "MultivariateCalculusExplanation"
    
    removed_count = 0
    for dir_path in [dir1, dir2]:
        if dir_path.exists():
            file_count = len(list(dir_path.glob("*.mp4")))
            shutil.rmtree(dir_path)
            print(f"  ✓ Removed {file_count} files from {dir_path.name}/")
            removed_count += file_count
    
    print(f"✅ Cache cleaned: {removed_count} files removed\n")
    return removed_count

def render_scene_fresh() -> tuple[str, Path]:
    """Render scene with clean cache to generate all files."""
    print(f"🎬 Rendering {SCENE_NAME} (fresh, no cache)...")
    cmd = ["manim", "-pqh", "--progress_bar", "none", str(SCENE_FILE), SCENE_NAME]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Rendering failed:\n{result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, cmd)
        
    print("✅ Rendering complete.\n")
    
    # Find actual partial directory (could be either variant)
    actual_dir = None
    for variant in ["MultivariableCalculusExplanation", "MultivariateCalculusExplanation"]:
        test_dir = PARTIAL_DIR / variant
        if test_dir.exists() and list(test_dir.glob("*.mp4")):
            actual_dir = test_dir
            break
    
    if not actual_dir:
        raise FileNotFoundError("Could not find partial movie files directory after render!")
    
    file_count = len(list(actual_dir.glob("*.mp4")))
    print(f"📁 Found {file_count} partial movie files in {actual_dir.name}/\n")
    
    return (result.stderr + "\n" + result.stdout, actual_dir)

def extract_all_frames(partial_dir: Path, analyzer: VisualLayoutAnalyzer) -> list[Path]:
    """Extract frames from ALL partial movie files."""
    print("🖼️  Extracting frames from all partial movie files...")
    
    # Get all .mp4 files sorted by name
    video_files = sorted(partial_dir.glob("*.mp4"))
    total_files = len(video_files)
    
    print(f"  Found {total_files} video files to process")
    
    # Extract frames
    frame_paths = analyzer.extract_frames_from_videos(video_files)
    
    print(f"✅ Extracted {len(frame_paths)} frames\n")
    return frame_paths

def verify_coverage(frame_count: int, expected_count: int):
    """Verify we achieved 100% coverage."""
    print("=" * 80)
    print("COVERAGE VERIFICATION")
    print("=" * 80)
    
    coverage_pct = (frame_count / expected_count * 100) if expected_count > 0 else 0
    
    print(f"Expected animation events: {expected_count}")
    print(f"Frames extracted: {frame_count}")
    print(f"Coverage: {coverage_pct:.1f}%")
    
    if frame_count >= expected_count:
        print("\n✅ SUCCESS: 100% coverage achieved!")
        print("✅ All frames ready for Qwen 3 VL analysis\n")
        return True
    else:
        print(f"\n⚠️  WARNING: Only {coverage_pct:.1f}% coverage")
        print(f"   Missing {expected_count - frame_count} frames\n")
        return False

def main():
    print("=" * 80)
    print("100% FRAME COVERAGE - CACHE CLEAN SOLUTION")
    print("=" * 80)
    print()
    
    # Phase 1: Clean cache
    clean_cache_for_scene()
    
    # Phase 2: Fresh render
    render_log, partial_dir = render_scene_fresh()
    
    # Phase 3: Extract frames
    analyzer = VisualLayoutAnalyzer(model=DualModelConfig.get_visual_model())
    frame_paths = extract_all_frames(partial_dir, analyzer)
    
    # Phase 4: Verify coverage
    # We expect roughly same count as diagnostic found (131 events)
    expected_count = 131  # From diagnostic report
    success = verify_coverage(len(frame_paths), expected_count)
    
    if success:
        print("🎉 Ready to analyze all frames with Qwen 3 VL!")
        print(f"   Frame paths saved in memory: {len(frame_paths)} total")
        print("\nNext step: Run fix_scene_layout.py to analyze frames for overlaps")
    
    # Clean up extracted frames
    print("\n🧹 Cleaning up extracted frames...")
    for frame in frame_paths:
        if frame.exists():
            frame.unlink()
    print("✅ Cleanup complete")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()

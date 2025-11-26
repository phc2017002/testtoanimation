#!/usr/bin/env python3
"""
Comprehensive frame analysis diagnostic for Binary Tree video.
Check all possible frame sources.
"""
from pathlib import Path
import subprocess

JOB_ID = "7603b84c-e63e-4dc1-ae5b-0847d36bcb6b"
SCENE_NAME = "BinaryTreeExplanation"

# Paths
VIDEO_DIR = Path(f"media/videos/scene_{JOB_ID}/1080p60")
PARTIAL_DIR = VIDEO_DIR / "partial_movie_files" / SCENE_NAME
VIDEO_FILE = VIDEO_DIR / f"{SCENE_NAME}.mp4"

print("=" * 80)
print("COMPREHENSIVE FRAME ANALYSIS DIAGNOSTIC")
print("=" * 80)
print()

# 1. Partial movie files
print("1. PARTIAL MOVIE FILES:")
print("-" * 80)
if PARTIAL_DIR.exists():
    partial_files = sorted(PARTIAL_DIR.glob("*.mp4"))
    print(f"Directory: {PARTIAL_DIR}")
    print(f"Total .mp4 files: {len(partial_files)}")
    print()
else:
    print(f"❌ Directory not found: {PARTIAL_DIR}")
    print()

# 2. Check for multiple scene directories
print("2. ALL SCENE DIRECTORIES IN PARTIAL_MOVIE_FILES:")
print("-" * 80)
pmf_base = VIDEO_DIR / "partial_movie_files"
if pmf_base.exists():
    for scene_dir in pmf_base.iterdir():
        if scene_dir.is_dir():
            mp4_count = len(list(scene_dir.glob("*.mp4")))
            print(f"  {scene_dir.name}: {mp4_count} files")
print()

# 3. Total video frames
print("3. TOTAL VIDEO FRAMES (at 60fps):")
print("-" * 80)
if VIDEO_FILE.exists():
    # Use ffprobe to get frame count
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", 
         "-count_frames", "-show_entries", "stream=nb_read_frames", 
         "-of", "csv=p=0", str(VIDEO_FILE)],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        frame_count = result.stdout.strip()
        print(f"Total frames in final video: {frame_count}")
        
        # Calculate duration
        dur_result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(VIDEO_FILE)],
            capture_output=True, text=True
        )
        if dur_result.returncode == 0:
            duration = float(dur_result.stdout.strip())
            print(f"Video duration: {duration:.2f} seconds")
            print(f"Expected frames at 60fps: {int(duration * 60)}")
    else:
        print("Could not count frames (ffprobe failed)")
else:
    print(f"❌ Video file not found: {VIDEO_FILE}")
print()

# 4. Scene code analysis
print("4. SCENE CODE ANALYSIS:")
print("-" * 80)
scene_file = Path(f"scene_{JOB_ID}.py")
if scene_file.exists():
    with open(scene_file) as f:
        content = f.read()
    
    play_count = content.count("self.play(")
    wait_count = content.count("self.wait(")
    
    print(f"self.play() calls: {play_count}")
    print(f"self.wait() calls: {wait_count}")
    print(f"Total animation commands: {play_count + wait_count}")
else:
    print(f"❌ Scene file not found: {scene_file}")
print()

print("=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)

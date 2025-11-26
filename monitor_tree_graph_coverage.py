#!/usr/bin/env python3
"""
Monitor Tree/Graph video job with DETAILED frame count tracking.
Verify that --disable_caching creates 200+ partial files (not just 100).
"""
import requests
import time
import json
from pathlib import Path

JOB_ID = "6edb1316-5c19-4406-a59b-86dddd8d8738"
API_URL = "http://localhost:8003"

def check_job_status():
    """Check job status and return current state."""
    response = requests.get(f"{API_URL}/api/jobs/{JOB_ID}")
    return response.json()

def count_partial_files(job_id):
    """Count partial movie files created so far."""
    # Try both possible scene name variants
    patterns = [
        f"media/videos/scene_{job_id}/1080p60/partial_movie_files/*/",
        f"media/videos/scene_{job_id}/1080p60/partial_movie_files/"
    ]
    
    for pattern in patterns:
        base_path = Path(pattern.replace("*", ""))
        if base_path.exists():
            for scene_dir in base_path.iterdir():
                if scene_dir.is_dir():
                    mp4_files = list(scene_dir.glob("*.mp4"))
                    return len(mp4_files), scene_dir.name
    
    return 0, None

def monitor_job():
    """Monitor job with detailed frame tracking."""
    print("=" * 80)
    print("MONITORING TREE/GRAPH VIDEO - TRUE 100% FRAME COVERAGE TEST")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
    print(f"GOAL: Verify 200+ frames analyzed (not just 100)")
    print()
    
    last_stage = None
    last_partial_count = 0
    start_time = time.time()
    
    while True:
        try:
            job = check_job_status()
            status = job.get('status')
            progress = job.get('progress', {})
            stage = progress.get('stage', 'unknown')
            percentage = progress.get('percentage', 0)
            message = progress.get('message', '')
            
            # Print updates when stage changes
            if stage != last_stage:
                elapsed = time.time() - start_time
                print(f"[{elapsed:.1f}s] {status.upper()}: {stage}")
                print(f"  └─ {message} ({percentage}%)")
                last_stage = stage
            
            # During rendering, check partial file count
            if status == 'rendering':
                partial_count, scene_name = count_partial_files(JOB_ID)
                if partial_count > last_partial_count:
                    print(f"  📊 Partial files: {partial_count} (previous: {last_partial_count})")
                    last_partial_count = partial_count
                    
                    # Alert if we hit 100 (old behavior)
                    if partial_count == 100:
                        print(f"  ⚠️  WARNING: Reached 100 files - checking if more...")
                    
                    # Celebrate if we exceed 100!
                    if partial_count == 101:
                        print(f"  🎉 SUCCESS: Exceeded 100 files! --disable_caching is working!")
            
            # Check if completed
            if status == 'completed':
                print()
                print("=" * 80)
                print("✅ JOB COMPLETED!")
                print("=" * 80)
                
                # Final partial file count
                final_partial_count, scene_name = count_partial_files(JOB_ID)
                print(f"\n📊 PARTIAL FILES CREATED: {final_partial_count}")
                
                # Check visual_analysis
                if 'visual_analysis' in job:
                    print("\n🎯 VISUAL ANALYSIS RESULTS:")
                    print("-" * 80)
                    va = job['visual_analysis']
                    frames_analyzed = va.get('frames_analyzed', 0)
                    print(f"Model: {va.get('model', 'N/A')}")
                    print(f"Frames Analyzed: {frames_analyzed}")
                    print(f"Overall Quality: {va.get('overall_quality', 'N/A')}")
                    print(f"Coverage: {va.get('coverage_percentage', 0)}%")
                    print(f"Issues Found: {len(va.get('issues', []))}")
                    
                    # CRITICAL CHECK
                    print()
                    print("=" * 80)
                    print("COVERAGE VERIFICATION")
                    print("=" * 80)
                    print(f"Partial files created: {final_partial_count}")
                    print(f"Frames analyzed: {frames_analyzed}")
                    
                    if frames_analyzed >= 200:
                        print("\n✅ ✅ ✅ SUCCESS! TRUE 100% COVERAGE ACHIEVED!")
                        print(f"   Analyzed {frames_analyzed} frames (expected 200+)")
                        print("   --disable_caching is working perfectly!")
                    elif frames_analyzed == 100:
                        print("\n❌ ❌ ❌ FAILURE! Still only 100 frames!")
                        print("   --disable_caching may not be working")
                        print("   Check api_server.py implementation")
                    else:
                        print(f"\n⚠️  Analyzed {frames_analyzed} frames")
                        print(f"   Expected: 200+ (got {frames_analyzed})")
                    
                    print("=" * 80)
                else:
                    print("\n❌ WARNING: No visual_analysis data found!")
                
                return job
            
            # Check if failed
            if status == 'failed':
                print()
                print("❌ JOB FAILED!")
                print(f"Error: {job.get('error', 'Unknown error')}")
                return job
            
            # Wait before next check
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\n\nMonitoring interrupted by user.")
            return None
        except Exception as e:
            print(f"Error checking status: {e}")
            time.sleep(5)

if __name__ == "__main__":
    result = monitor_job()
    
    if result:
        # Save full job data
        with open(f"job_{JOB_ID}_coverage_test.json", "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nFull job data saved to: job_{JOB_ID}_coverage_test.json")

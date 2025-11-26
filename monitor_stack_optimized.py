#!/usr/bin/env python3
"""
Monitor Stack/Linked List video - VERIFY OPTIMIZED PERFORMANCE
Job ID: b70907f9-5e95-471a-a4d2-7180bbe01a24

This test verifies:
1. Faster verification (2 iterations instead of 5)
2. Timestamp-based extraction analyzes 200+ frames 
3. Overall time improved by ~40%
"""
import requests
import time
import json
from pathlib import Path
from datetime import datetime

JOB_ID = "b70907f9-5e95-471a-a4d2-7180bbe01a24"
API_URL = "http://localhost:8003"

def check_job_status():
    """Check job status and return current state."""
    response = requests.get(f"{API_URL}/api/jobs/{JOB_ID}")
    return response.json()

def monitor_job():
    """Monitor job with performance tracking."""
    print("=" * 80)
    print("MONITORING STACK/LINKED LIST VIDEO - OPTIMIZED PERFORMANCE TEST")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("OPTIMIZATION GOALS:")
    print("  1. Verification loop: 2 iterations (was 5)")
    print("  2. Timestamp extraction: 200+ frames analyzed")
    print("  3. Total time: ~30-50 min (was 50-95 min)")
    print("=" * 80)
    print()
    
    last_stage = None
    start_time = time.time()
    verification_start = None
    verification_attempts = 0
    
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
                print(f"[{elapsed/60:.1f}m] {status.upper()}: {stage}")
                print(f"  └─ {message} ({percentage}%)")
                
                # Track verification start
                if stage == 'verifying' and verification_start is None:
                    verification_start = time.time()
                
                last_stage = stage
            
            # Count verification attempts
            if 'Attempt' in message:
                import re
                match = re.search(r'Attempt (\d+)/(\d+)', message)
                if match:
                    current_attempt = int(match.group(1))
                    max_attempts = int(match.group(2))
                    if current_attempt > verification_attempts:
                        verification_attempts = current_attempt
                        elapsed = time.time() - start_time
                        print(f"  🔄 Verification attempt {current_attempt}/{max_attempts} (elapsed: {elapsed/60:.1f}m)")
                        
                        # Check if it's 2 iterations as expected
                        if max_attempts == 2:
                            print(f"  ✅ Optimized: 2 max attempts (was 5)")
                        elif max_attempts > 2:
                            print(f"  ⚠️  Still {max_attempts} max attempts (expected 2)")
            
            # Check if completed
            if status == 'completed':
                total_time = time.time() - start_time
                verification_time = (time.time() - verification_start) if verification_start else 0
                
                print()
                print("=" * 80)
                print("✅ JOB COMPLETED!")
                print("=" * 80)
                print(f"Total Time: {total_time/60:.1f} minutes")
                print(f"Verification Time: {verification_time/60:.1f} minutes")
                print(f"Verification Attempts: {verification_attempts}")
                print()
                
                # Performance check
                if total_time < 3000:  # < 50 minutes
                    print("✅ Performance: GOOD (< 50 min)")
                elif total_time < 3600:  # < 60 minutes
                    print("⚠️  Performance: OK (50-60 min)")
                else:
                    print("❌ Performance: SLOW (> 60 min)")
                print()
                
                # Visual analysis check
                if 'visual_analysis' in job:
                    print("🎯 VISUAL ANALYSIS RESULTS:")
                    print("-" * 80)
                    va = job['visual_analysis']
                    
                    frames = va.get('frames_analyzed', 0)
                    total_anims = va.get('total_animations', 0)
                    method = va.get('extraction_method', 'N/A')
                    
                    print(f"Extraction Method: {method}")
                    print(f"Total Animations: {total_anims}")
                    print(f"Frames Analyzed: {frames}")
                    print(f"Overall Quality: {va.get('overall_quality', 'N/A')}")
                    print(f"Issues Found: {len(va.get('issues', []))}")
                    print()
                    
                    # Verification
                    print("=" * 80)
                    print("VERIFICATION RESULTS")
                    print("=" * 80)
                    
                    # Check 1: Method
                    if method == 'timestamp_based':
                        print("✅ Method: timestamp_based")
                    else:
                        print(f"⚠️  Method: {method} (expected timestamp_based)")
                    
                    # Check 2: Frame count
                    if frames >= 200:
                        print(f"✅ Frames: {frames} (200+ achieved!)")
                    elif frames > 100:
                        print(f"⚠️  Frames: {frames} (> 100 but < 200)")
                    else:
                        print(f"❌ Frames: {frames} (still only 100!)")
                    
                    # Check 3: Verification attempts
                    if verification_attempts <= 2:
                        print(f"✅ Attempts: {verification_attempts} (optimized)")
                    else:
                        print(f"⚠️  Attempts: {verification_attempts} (expected ≤ 2)")
                    
                    # Final verdict
                    print()
                    if method == 'timestamp_based' and frames >= 200 and total_time < 3000:
                        print("🎉 🎉 🎉 ALL OPTIMIZATIONS WORKING! 🎉 🎉 🎉")
                    else:
                        print("⚠️  Some optimizations may need adjustment")
                    
                    print("=" * 80)
                else:
                    print("\n❌ No visual_analysis data found")
                
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
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    result = monitor_job()
    
    if result:
        # Save results
        with open(f"job_{JOB_ID}_optimized_test.json", "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to: job_{JOB_ID}_optimized_test.json")

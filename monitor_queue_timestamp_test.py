#!/usr/bin/env python3
"""
Monitor Queue/Linked List video job - VERIFY TRUE 100% FRAME COVERAGE
Job ID: 2facb1ce-0243-4c52-b664-328aae1fff8d

This test verifies the new timestamp-based extraction analyzes ALL frames (200+, not just 100).
"""
import requests
import time
import json
from pathlib import Path

JOB_ID = "2facb1ce-0243-4c52-b664-328aae1fff8d"
API_URL = "http://localhost:8003"

def check_job_status():
    """Check job status and return current state."""
    response = requests.get(f"{API_URL}/api/jobs/{JOB_ID}")
    return response.json()

def monitor_job():
    """Monitor job with focus on frame coverage verification."""
    print("=" * 80)
    print("MONITORING QUEUE/LINKED LIST VIDEO - TRUE 100% FRAME COVERAGE TEST")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
    print(f"GOAL: Verify timestamp-based extraction analyzes 200+ frames (not 100)")
    print()
    
    last_stage = None
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
            
            # Check if completed
            if status == 'completed':
                print()
                print("=" * 80)
                print("✅ JOB COMPLETED!")
                print("=" * 80)
                
                # CRITICAL: Check visual_analysis
                if 'visual_analysis' in job:
                    print("\n🎯 VISUAL ANALYSIS RESULTS:")
                    print("-" * 80)
                    va = job['visual_analysis']
                    
                    frames_analyzed = va.get('frames_analyzed', 0)
                    total_animations = va.get('total_animations', 0)
                    extraction_method = va.get('extraction_method', 'unknown')
                    
                    print(f"Model: {va.get('model', 'N/A')}")
                    print(f"Extraction Method: {extraction_method}")
                    print(f"Total Animations: {total_animations}")
                    print(f"Frames Analyzed: {frames_analyzed}")
                    print(f"Overall Quality: {va.get('overall_quality', 'N/A')}")
                    print(f"Coverage: {va.get('coverage_percentage', 0)}%")
                    print(f"Issues Found: {len(va.get('issues', []))}")
                    
                    # VERIFICATION
                    print()
                    print("=" * 80)
                    print("TIMESTAMP-BASED EXTRACTION VERIFICATION")
                    print("=" * 80)
                    
                    # Check 1: Method used
                    if extraction_method == "timestamp_based":
                        print("✅ Method: timestamp_based (correct!)")
                    else:
                        print(f"❌ Method: {extraction_method} (should be timestamp_based)")
                    
                    # Check 2: Frame count
                    if frames_analyzed >= 200:
                        print(f"✅ Frames: {frames_analyzed} (200+ achieved!)")
                        print("\n🎉 🎉 🎉 SUCCESS! TRUE 100% COVERAGE ACHIEVED! 🎉 🎉 🎉")
                    elif frames_analyzed > 100:
                        print(f"⚠️  Frames: {frames_analyzed} (better than 100 but < 200)")
                    elif frames_analyzed == 100:
                        print(f"❌ Frames: {frames_analyzed} (still only 100 - FAILED)")
                        print("    Timestamp-based extraction may not be working!")
                    else:
                        print(f"⚠️  Frames: {frames_analyzed} (unexpected count)")
                    
                    # Check 3: Coverage vs Total
                    if total_animations > 0:
                        coverage = (frames_analyzed / total_animations) * 100
                        print(f"\nActual Coverage: {frames_analyzed}/{total_animations} = {coverage:.1f}%")
                        
                        if coverage >= 99:
                            print("✅ Coverage: TRUE 100%!")
                        elif coverage >= 80:
                            print("⚠️  Coverage: Partial (need investigation)")
                        else:
                            print("❌ Coverage: Poor (< 80%)")
                    
                    print("=" * 80)
                    
                    # Show issues if any
                    if va.get('issues'):
                        print("\nDETECTED ISSUES:")
                        print("-" * 80)
                        for i, issue in enumerate(va['issues'][:5], 1):  # Show first 5
                            print(f"{i}. [{issue.get('severity', 'N/A')}] {issue.get('type', 'unknown')}")
                            print(f"   {issue.get('description', 'No description')}")
                        
                        if len(va['issues']) > 5:
                            print(f"... and {len(va['issues']) - 5} more issues")
                    
                else:
                    print("\n❌ WARNING: No visual_analysis data found!")
                    print("   The comprehensive analysis may have failed.")
                
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
        with open(f"job_{JOB_ID}_timestamp_test.json", "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nFull job data saved to: job_{JOB_ID}_timestamp_test.json")

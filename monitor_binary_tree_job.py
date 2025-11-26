#!/usr/bin/env python3
"""
Monitor Binary Tree video job and verify Qwen 3 VL analysis.
Job ID: 7603b84c-e63e-4dc1-ae5b-0847d36bcb6b
"""
import requests
import time
import json

JOB_ID = "7603b84c-e63e-4dc1-ae5b-0847d36bcb6b"
API_URL = "http://localhost:8003"

def check_job_status():
    """Check job status and return current state."""
    response = requests.get(f"{API_URL}/api/jobs/{JOB_ID}")
    return response.json()

def monitor_job():
    """Monitor job until completion and verify visual analysis."""
    print("=" * 80)
    print("MONITORING BINARY TREE VIDEO GENERATION")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
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
                
                # Check for visual_analysis
                if 'visual_analysis' in job:
                    print("\n🎯 VISUAL ANALYSIS RESULTS:")
                    print("-" * 80)
                    va = job['visual_analysis']
                    print(f"Model: {va.get('model', 'N/A')}")
                    print(f"Frames Analyzed: {va.get('frames_analyzed', 0)}")
                    print(f"Overall Quality: {va.get('overall_quality', 'N/A')}")
                    print(f"Coverage: {va.get('coverage_percentage', 0)}%")
                    print(f"Issues Found: {len(va.get('issues', []))}")
                    
                    if va.get('issues'):
                        print("\nDETECTED ISSUES:")
                        for i, issue in enumerate(va['issues'], 1):
                            print(f"{i}. [{issue.get('severity', 'N/A')}] {issue.get('type', 'unknown')}")
                            print(f"   {issue.get('description', 'No description')}")
                    else:
                        print("\n✅ No layout issues detected!")
                    
                    print()
                    print("=" * 80)
                    print(f"✅ SUCCESS: All {va.get('frames_analyzed', 0)} frames verified by Qwen 3 VL!")
                    print("=" * 80)
                else:
                    print("\n❌ WARNING: No visual_analysis data found in job!")
                    print("   The automatic analysis may have failed.")
                
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
        with open(f"job_{JOB_ID}_result.json", "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nFull job data saved to: job_{JOB_ID}_result.json")

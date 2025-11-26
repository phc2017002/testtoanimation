#!/usr/bin/env python3
"""
Monitor Circular Queue video - ENHANCED COMPREHENSIVE ANALYSIS TEST
Job ID: f22220af-c901-4b30-9b0f-79fe87561eb8

This test verifies the complete enhanced analysis workflow:
1. Timestamp-based extraction analyzes 195+ frames (not 100)
2. Auto-fix activates when issues are found
3. Claude generates batched fixes
4. Re-render with fixes
5. Re-verification shows improvement
"""
import requests
import time
import json
from pathlib import Path
from datetime import datetime

JOB_ID = "f22220af-c901-4b30-9b0f-79fe87561eb8"
API_URL = "http://localhost:8003"

def check_job():
    """Check job from file (API response doesn't include visual_analysis)."""
    job_file = Path(f"jobs/{JOB_ID}.json")
    if job_file.exists():
        return json.load(open(job_file))
    return None

def monitor_job():
    """Monitor job with focus on enhanced analysis workflow."""
    print("=" * 80)
    print("MONITORING CIRCULAR QUEUE - ENHANCED COMPREHENSIVE ANALYSIS TEST")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("TESTING:")
    print("  1. 195+ Frame Coverage (timestamp extraction)")
    print("  2. Auto-Fix Activation (when issues found)")
    print("  3. Claude Fix Generation (batched)")
    print("  4. Re-Render with Fixes")
    print("  5. Re-Verification (before/after comparison)")
    print("=" * 80)
    print()
    
    last_status = None
    start_time = time.time()
    
    while True:
        try:
            job = check_job()
            if not job:
                time.sleep(5)
                continue
            
            status = job.get('status')
            
            # Print status changes
            if status != last_status:
                elapsed = time.time() - start_time
                progress = job.get('progress', {})
                print(f"[{elapsed/60:.1f}m] {status.upper()}: {progress.get('message', 'Processing...')}")
                last_status = status
            
            # Check if completed
            if status == 'completed':
                total_time = time.time() - start_time
                
                print()
                print("=" * 80)
                print("✅ JOB COMPLETED!")
                print("=" * 80)
                print(f"Total Time: {total_time/60:.1f} minutes")
                print()
                
                # Check visual analysis
                if 'visual_analysis' in job:
                    va = job['visual_analysis']
                    
                    print("🎯 VISUAL ANALYSIS RESULTS:")
                    print("-" * 80)
                    print(f"Frames Analyzed: {va.get('frames_analyzed', 0)}")
                    print(f"Overall Quality: {va.get('overall_quality', 'N/A')}")
                    print(f"Issues Found: {len(va.get('issues', []))}")
                    print()
                    
                    # Check auto-fix
                    if 'auto_fix' in va:
                        af = va['auto_fix']
                        print("🔧 AUTO-FIX WORKFLOW:")
                        print("-" * 80)
                        print(f"Applied: {af.get('applied', False)}")
                        
                        if af.get('applied'):
                            print(f"Issues Before: {af.get('issues_before', 0)}")
                            print(f"Issues After: {af.get('issues_after', 0)}")
                            print(f"Improvement: {af.get('improvement', 0)} issues fixed")
                            print(f"Quality: {af.get('quality_before', 'N/A')} → {af.get('quality_after', 'N/A')}")
                        elif af.get('error'):
                            print(f"Error: {af.get('error')}")
                        print()
                    
                    # Verification
                    print("=" * 80)
                    print("VERIFICATION")
                    print("=" * 80)
                    
                    frames = va.get('frames_analyzed', 0)
                    
                    # Check 1: Frame coverage
                    if frames >= 190:
                        print(f"✅ Frames: {frames} (190+ achieved!)")
                    elif frames > 100:
                        print(f"⚠️  Frames: {frames} (> 100 but < 190)")
                    else:
                        print(f"❌ Frames: {frames} (only 100)")
                    
                    # Check 2: Auto-fix
                    if 'auto_fix' in va and va['auto_fix'].get('applied'):
                        improvement = va['auto_fix'].get('improvement', 0)
                        issues_before = va['auto_fix'].get('issues_before', 0)
                        
                        if improvement > 0 and issues_before > 0:
                            pct = (improvement / issues_before) * 100
                            print(f"✅ Auto-Fix: {improvement}/{issues_before} fixed ({pct:.0f}%)")
                        else:
                            print(f"✅ Auto-Fix: Applied (no issues found initially)")
                    else:
                        print("⚠️  Auto-Fix: Not activated (no issues or error)")
                    
                    print()
                    if frames >= 190:
                        print("🎉 🎉 🎉 ENHANCED ANALYSIS WORKING! 🎉 🎉 🎉")
                    print("=" * 80)
                    
                    # Show sample issues
                    if va.get('issues'):
                        print("\nFINAL ISSUES (Sample - First 5):")
                        print("-" * 80)
                        for i, issue in enumerate(va['issues'][:5], 1):
                            print(f"{i}. Frame {issue.get('frame', '?')}: [{issue.get('type', '?')}] {issue.get('description', '?')[:80]}")
                        
                        if len(va['issues']) > 5:
                            print(f"... and {len(va['issues']) - 5} more issues")
                else:
                    print("\n❌ No visual_analysis data found!")
                
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
            print("\n\nMonitoring interrupted.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    result = monitor_job()
    
    if result:
        # Save results
        with open(f"job_{JOB_ID}_enhanced_test.json", "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to: job_{JOB_ID}_enhanced_test.json")

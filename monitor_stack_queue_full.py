#!/usr/bin/env python3
"""
Monitor Stack/Queue video - COMPLETE AUTO-FIX WORKFLOW TEST
Job ID: 1bbbfa03-3ef4-4a57-bba6-55fb9d52ffb1

This is the COMPLETE test of enhanced comprehensive analysis with auto-fix:
1. 220+ Frame Coverage (timestamp extraction)
2. Issue Detection (Qwen 3 VL)
3. Auto-Fix Activation (CORRECTED logic: len(issues) > 0)
4. Claude Fix Generation (batched fixes for all issues)
5. Re-Render with Fixes
6. Re-Verification (before/after comparison)
"""
import requests
import time
import json
from pathlib import Path
from datetime import datetime

JOB_ID = "1bbbfa03-3ef4-4a57-bba6-55fb9d52ffb1"
API_URL = "http://localhost:8003"

def check_job():
    """Check job from file."""
    job_file = Path(f"jobs/{JOB_ID}.json")
    if job_file.exists():
        return json.load(open(job_file))
    return None

def monitor_job():
    """Monitor complete auto-fix workflow."""
    print("=" * 80)
    print("MONITORING STACK/QUEUE - COMPLETE AUTO-FIX WORKFLOW TEST")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("COMPLETE WORKFLOW TO VERIFY:")
    print("  1. ✓ Frame Coverage: 220+ frames (timestamp extraction)")
    print("  2. ✓ Issue Detection: Qwen 3 VL finds overlaps/issues")
    print("  3. ✓ Auto-Fix Activation: len(issues) > 0 (CORRECTED)")
    print("  4. ✓ Claude Fix Generation: Batched fixes")
    print("  5. ✓ Re-Render: Apply all fixes")
    print("  6. ✓ Re-Verification: Confirm improvement")
    print("=" * 80)
    print()
    
    last_status = None
    start_time = time.time()
    auto_fix_detected = False
    
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
                msg = progress.get('message', 'Processing...')
                print(f"[{elapsed/60:.1f}m] {status.upper()}: {msg}")
                last_status = status
                
                # Detect auto-fix in progress
                if 'auto' in msg.lower() or 'fix' in msg.lower():
                    auto_fix_detected = True
                    print(f"  🔧 AUTO-FIX DETECTED IN PROGRESS!")
            
            # Check if completed
            if status == 'completed':
                total_time = time.time() - start_time
                
                print()
                print("=" * 80)
                print("✅ JOB COMPLETED!")
                print("=" * 80)
                print(f"Total Time: {total_time/60:.1f} minutes")
                print()
                
                # Comprehensive results
                if 'visual_analysis' in job:
                    va = job['visual_analysis']
                    
                    print("📊 VISUAL ANALYSIS RESULTS:")
                    print("-" * 80)
                    print(f"Frames Analyzed: {va.get('frames_analyzed', 0)}")
                    print(f"Overall Quality: {va.get('overall_quality', 'N/A')}")
                    print(f"Issues Found (Final): {len(va.get('issues', []))}")
                    print()
                    
                    # Check auto-fix results
                    if 'auto_fix' in va:
                        af = va['auto_fix']
                        print("🔧 AUTO-FIX WORKFLOW RESULTS:")
                        print("-" * 80)
                        print(f"✅ Applied: {af.get('applied', False)}")
                        
                        if af.get('applied'):
                            before = af.get('issues_before', 0)
                            after = af.get('issues_after', 0)
                            improvement = af.get('improvement', 0)
                            
                            print(f"Issues Before: {before}")
                            print(f"Issues After: {after}")
                            print(f"Issues Fixed: {improvement}")
                            print(f"Quality: {af.get('quality_before')} → {af.get('quality_after')}")
                            
                            if before > 0:
                                pct = (improvement / before) * 100
                                print(f"Success Rate: {pct:.1f}%")
                                print()
                                
                                if pct >= 80:
                                    print("🎉 EXCELLENT FIX RATE (80%+)!")
                                elif pct >= 50:
                                    print("✅ GOOD FIX RATE (50-80%)")
                                else:
                                    print("⚠️  MODERATE FIX RATE (<50%)")
                        elif af.get('error'):
                            print(f"❌ Error: {af.get('error')}")
                        print()
                    else:
                        print("⚠️  AUTO-FIX: Not present in results")
                        print()
                    
                    # Verification
                    print("=" * 80)
                    print("FINAL VERIFICATION")
                    print("=" * 80)
                    
                    frames = va.get('frames_analyzed', 0)
                    
                    # Check 1: Frame coverage
                    if frames >= 200:
                        print(f"✅ Frame Coverage: {frames} frames (200+ achieved!)")
                    else:
                        print(f"⚠️  Frame Coverage: {frames} frames (< 200)")
                    
                    # Check 2: Auto-fix activation
                    if 'auto_fix' in va and va['auto_fix'].get('applied'):
                        print("✅ Auto-Fix: Activated and completed")
                        
                        # Check 3: Improvement
                        improvement = va['auto_fix'].get('improvement', 0)
                        if improvement > 0:
                            print(f"✅ Improvement: {improvement} issues fixed")
                        else:
                            print("⚠️  Improvement: No issues fixed")
                    else:
                        issues = len(va.get('issues', []))
                        if issues > 0:
                            print(f"❌ Auto-Fix: NOT activated (but {issues} issues found!)")
                        else:
                            print("✅ Auto-Fix: Not needed (no issues found)")
                    
                    print()
                    print("=" * 80)
                    
                    # Final verdict
                    if (frames >= 200 and 
                        'auto_fix' in va and 
                        va['auto_fix'].get('applied') and 
                        va['auto_fix'].get('improvement', 0) > 0):
                        print("🎉 🎉 🎉 COMPLETE SUCCESS! ALL SYSTEMS WORKING! 🎉 🎉 🎉")
                        print()
                        print("✓ 200+ Frame Coverage")
                        print("✓ Auto-Fix Activated")
                        print("✓ Fixes Applied Successfully")
                        print("✓ Improvement Verified")
                    else:
                        print("⚠️  PARTIAL SUCCESS - Review results above")
                    
                    print("=" * 80)
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
        with open(f"job_{JOB_ID}_complete_test.json", "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to: job_{JOB_ID}_complete_test.json")

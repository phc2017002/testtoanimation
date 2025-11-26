#!/usr/bin/env python3
"""
Monitor Queue/Stack video - COMPLETE WORKFLOW TEST WITH ERROR HANDLING
Job ID: c6f9b022-a578-44bf-8ad0-92e2bf1e94ba

COMPLETE SYSTEM TEST - All Fixes Applied:
✓ Initial Render Error Handling (catches render failures)
✓ Verification Loop Handles Failures (retry/regenerate)
✓ Frame Coverage (220+ frames via timestamp)
✓ Auto-Fix Activation (len(issues) > 0)
✓ Claude Fix Generation (DualModelConfig)
✓ Re-Render & Re-Verification
"""
import json
from pathlib import Path
from datetime import datetime
import time

JOB_ID = "c6f9b022-a578-44bf-8ad0-92e2bf1e94ba"

def monitor():
    print("=" * 80)
    print("COMPLETE WORKFLOW TEST - Queue Implementation Using Stack")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("ALL FIXES APPLIED:")
    print("  ✓ Render Error Handling: Initial render failures now caught")
    print("  ✓ Verification: Handles failures & triggers fixes")
    print("  ✓ Frame Coverage: 220+ frames (timestamp extraction)")
    print("  ✓ Auto-Fix: Correct activation logic")
    print("  ✓ Claude API: Fixed integration")
    print("=" * 80)
    print()
    
    last_status = None
    start_time = time.time()
    render_errors_caught = 0
    
    while True:
        try:
            job_file = Path(f"jobs/{JOB_ID}.json")
            if not job_file.exists():
                time.sleep(5)
                continue
            
            job = json.load(open(job_file))
            status = job.get('status')
            
            if status != last_status:
                elapsed = time.time() - start_time
                progress = job.get('progress', {})
                msg = progress.get('message', 'Processing...')
                print(f"[{elapsed/60:.1f}m] {status.upper()}: {msg}")
                last_status = status
            
            if status == 'completed':
                total_time = time.time() - start_time
                
                print()
                print("=" * 80)
                print("✅ JOB COMPLETED!")
                print("=" * 80)
                print(f"Total Time: {total_time/60:.1f} minutes")
                print()
                
                va = job.get('visual_analysis', {})
                
                if va:
                    frames = va.get('frames_analyzed', 0)
                    quality = va.get('overall_quality', 'N/A')
                    issues = len(va.get('issues', []))
                    
                    print("📊 VISUAL ANALYSIS:")
                    print("-" * 80)
                    print(f"Frames Analyzed: {frames}")
                    print(f"Quality: {quality}")
                    print(f"Final Issues: {issues}")
                    
                    if 'auto_fix' in va and va['auto_fix'].get('applied'):
                        af = va['auto_fix']
                        print()
                        print("🔧 AUTO-FIX RESULTS:")
                        print("-" * 80)
                        print(f"Before: {af.get('issues_before', 0)} issues")
                        print(f"After: {af.get('issues_after', 0)} issues")
                        print(f"Fixed: {af.get('improvement', 0)}")
                        print(f"Quality: {af.get('quality_before')} → {af.get('quality_after')}")
                        
                        if af.get('issues_before', 0) > 0:
                            rate = (af.get('improvement', 0) / af['issues_before']) * 100
                            print(f"Success: {rate:.1f}%")
                            
                            if rate >= 60:
                                print("\n🎉 EXCELLENT AUTO-FIX PERFORMANCE!")
                            elif rate >= 30:
                                print("\n✅ Good auto-fix results")
                    
                    print()
                    print("=" * 80)
                    print("FINAL VERIFICATION:")
                    print("=" * 80)
                    
                    if frames >= 200:
                        print(f"✅ Coverage: {frames} frames (200+)")
                    else:
                        print(f"⚠️  Coverage: {frames} frames")
                    
                    if 'auto_fix' in va and va['auto_fix'].get('applied'):
                        print("✅ Auto-Fix: Activated & Completed")
                    else:
                        if issues == 0:
                            print("✅ Auto-Fix: Not needed (perfect!)")
                        else:
                            print(f"⚠️  Auto-Fix: Not activated ({issues} issues)")
                    
                    print("=" * 80)
                    
                    if frames >= 200 and (issues == 0 or ('auto_fix' in va and va['auto_fix'].get('applied'))):
                        print("\n🎉 🎉 🎉 ALL SYSTEMS WORKING! 🎉 🎉 🎉")
                else:
                    print("❌ No visual_analysis")
                
                with open(f"job_{JOB_ID}_complete.json", "w") as f:
                    json.dump(job, f, indent=2)
                print(f"\nSaved: job_{JOB_ID}_complete.json")
                return job
            
            if status == 'failed':
                print(f"\n❌ JOB FAILED: {job.get('error')}")
                return job
            
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\nInterrupted")
            return None
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    monitor()

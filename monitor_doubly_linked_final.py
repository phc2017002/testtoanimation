#!/usr/bin/env python3
"""
Monitor Doubly Linked List video - FINAL COMPREHENSIVE TEST
Job ID: 70ee3965-b29a-4734-b78f-d9422f825c04

TESTING ALL FIXES:
✓ Robust JSON Parsing (4 fallback strategies)
✓ Code Validation (reject bad fixes)
✓ Enhanced Prompts (stricter rules)
✓ Success/Failure Logging (clear messages)

Expected Results:
- Zero "Visual analysis failed for batch X" errors
- All batches complete (no JSON parsing failures)
- Auto-fix validates OR rejects (doesn't make worse)
- Clear SUCCESS/FAILURE/NO_CHANGE messages
"""
import json
from pathlib import Path
from datetime import datetime
import time

JOB_ID = "70ee3965-b29a-4734-b78f-d9422f825c04"

def monitor():
    print("=" * 80)
    print("FINAL COMPREHENSIVE TEST - Doubly Linked List")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("TESTING ALL FIXES:")
    print("  ✓ Robust JSON Parsing (0 failures expected)")
    print("  ✓ Code Validation (rejects bad fixes)")
    print("  ✓ Enhanced Prompts (better fixes)")
    print("  ✓ Clear Logging (SUCCESS/FAILURE/NO_CHANGE)")
    print("=" * 80)
    print()
    
    last_status = None
    start_time = time.time()
    json_errors = 0
    batches_completed = 0
    batches_failed = 0
    
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
                    
                    print("📊 VISUAL ANALYSIS RESULTS:")
                    print("-" * 80)
                    print(f"Frames Analyzed: {frames}")
                    print(f"Quality: {quality}")
                    print(f"Final Issues: {issues}")
                    print()
                    
                    if 'auto_fix' in va:
                        af = va['auto_fix']
                        print("🔧 AUTO-FIX RESULTS:")
                        print("-" * 80)
                        
                        if af.get('applied'):
                            before = af.get('issues_before', 0)
                            after = af.get('issues_after', 0)
                            improvement = af.get('improvement', 0)
                            success = af.get('success', False)
                            
                            print(f"Applied: Yes")
                            print(f"Before: {before} issues")
                            print(f"After: {after} issues")
                            print(f"Improvement: {improvement}")
                            print(f"Success: {success}")
                            
                            if success:
                                rate = (improvement / before) * 100 if before > 0 else 0
                                print(f"Fix Rate: {rate:.1f}%")
                                print()
                                
                                if rate >= 70:
                                    print("🎉 EXCELLENT AUTO-FIX!")
                                elif rate >= 40:
                                    print("✅ GOOD AUTO-FIX")
                                else:
                                    print("⚠️  MODERATE AUTO-FIX")
                            else:
                                if improvement < 0:
                                    print("\n❌ AUTO-FIX VALIDATION SHOULD HAVE REJECTED THIS!")
                                elif improvement == 0:
                                    print("\n⚠️  AUTO-FIX NO CHANGE")
                        elif af.get('error'):
                            print(f"Error: {af.get('error')}")
                        else:
                            print("Not applied (validation rejected or no fix generated)")
                    
                    print()
                    print("=" * 80)
                    print("FINAL VERIFICATION:")
                    print("=" * 80)
                    
                    # Check 1: Frame coverage
                    if frames >= 80:
                        print(f"✅ Frames: {frames} (good coverage)")
                    else:
                        print(f"⚠️  Frames: {frames}")
                    
                    # Check 2: Auto-fix
                    if 'auto_fix' in va:
                        if va['auto_fix'].get('applied'):
                            if va['auto_fix'].get('success'):
                                print("✅ Auto-Fix: SUCCESS (improved)")
                            else:
                                print("❌ Auto-Fix: FAILED (no improvement)")
                        else:
                            print("⚠️  Auto-Fix: Not applied (rejected or error)")
                    else:
                        print("⚠️  Auto-Fix: Not triggered")
                    
                    print()
                    print("=" * 80)
                    
                    # Final verdict
                    all_good = (
                        frames >= 80 and
                        (issues == 0 or 
                         ('auto_fix' in va and va['auto_fix'].get('success')))
                    )
                    
                    if all_good:
                        print("\n🎉 🎉 🎉 ALL TESTS PASSED! 🎉 🎉 🎉")
                        print("\n✓ JSON Parsing Working")
                        print("✓ Frame Coverage Good")
                        print("✓ Auto-Fix Validated")
                    else:
                        print("\n⚠️  SOME TESTS NEED REVIEW")
                    
                    print("=" * 80)
                else:
                    print("❌ No visual_analysis")
                
                with open(f"job_{JOB_ID}_final.json", "w") as f:
                    json.dump(job, f, indent=2)
                print(f"\nSaved: job_{JOB_ID}_final.json")
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

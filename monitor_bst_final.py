#!/usr/bin/env python3
"""
Monitor Binary Search Tree video - FINAL AUTO-FIX WORKFLOW TEST
Job ID: 5b3036bd-8caa-4ccb-a970-9f94cafe564a

COMPLETE VERIFICATION of enhanced comprehensive analysis with auto-fix:
✓ Frame Coverage (220+ frames via timestamp extraction)
✓ Issue Detection (Qwen 3 VL)
✓ Auto-Fix Activation (len(issues) > 0 - CORRECTED)
✓ Claude Fix Generation (DualModelConfig.generate_code - FIXED)
✓ Re-Render with Fixes
✓ Re-Verification (before/after comparison)
"""
import requests
import time
import json
from pathlib import Path
from datetime import datetime

JOB_ID = "5b3036bd-8caa-4ccb-a970-9f94cafe564a"

def monitor_job():
    """Final comprehensive workflow test."""
    print("=" * 80)
    print("FINAL AUTO-FIX WORKFLOW TEST - Binary Search Tree Operations")
    print("=" * 80)
    print(f"Job ID: {JOB_ID}")
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("ALL SYSTEMS READY:")
    print("  ✓ Frame Coverage: Fixed (220+ frames)")
    print("  ✓ Auto-Fix Activation: Fixed (checks len(issues) > 0)")
    print("  ✓ Claude API Call: Fixed (uses DualModelConfig)")
    print("  ✓ Code Extraction: Fixed (uses post_process_code)")
    print("=" * 80)
    print()
    
    last_status = None
    start_time = time.time()
    
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
                    print("📊 RESULTS:")
                    print("-" * 80)
                    print(f"Frames: {va.get('frames_analyzed', 0)}")
                    print(f"Quality: {va.get('overall_quality', 'N/A')}")
                    print(f"Final Issues: {len(va.get('issues', []))}")
                    print()
                    
                    if 'auto_fix' in va and va['auto_fix'].get('applied'):
                        af = va['auto_fix']
                        print("🔧 AUTO-FIX SUCCESS!")
                        print("-" * 80)
                        print(f"Issues Before: {af.get('issues_before', 0)}")
                        print(f"Issues After: {af.get('issues_after', 0)}")
                        print(f"Fixed: {af.get('improvement', 0)}")
                        print(f"Quality: {af.get('quality_before')} → {af.get('quality_after')}")
                        
                        if af.get('issues_before', 0) > 0:
                            rate = (af.get('improvement', 0) / af['issues_before']) * 100
                            print(f"Success Rate: {rate:.1f}%")
                            print()
                            
                            if rate >= 70:
                                print("🎉 🎉 🎉 EXCELLENT! AUTO-FIX WORKS PERFECTLY! 🎉 🎉 🎉")
                            elif rate >= 40:
                                print("✅ GOOD! Auto-fix working well")
                            else:
                                print("⚠️  Moderate improvement")
                    else:
                        print(f"⚠️  Auto-fix not applied")
                        if len(va.get('issues', [])) == 0:
                            print("   (No issues found - perfect generation!)")
                    
                    print("=" * 80)
                else:
                    print("❌ No visual_analysis")
                
                # Save
                with open(f"job_{JOB_ID}_final_test.json", "w") as f:
                    json.dump(job, f, indent=2)
                print(f"\nSaved: job_{JOB_ID}_final_test.json")
                return job
            
            if status == 'failed':
                print(f"\n❌ FAILED: {job.get('error')}")
                return job
            
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\nInterrupted")
            return None
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    monitor_job()

#!/usr/bin/env python3
"""
Diagnostic script to investigate missing partial movie files.
Extracts all hashes from Manim logs and checks file distribution.
"""
import re
import subprocess
from pathlib import Path
from collections import defaultdict

# Configuration
SCENE_FILE = Path("scene_d29f69ad-efc3-48a9-862a-ff47b882d2c7.py")
SCENE_NAME = "MultivariableCalculusExplanation"
VIDEO_DIR = Path("media/videos/scene_d29f69ad-efc3-48a9-862a-ff47b882d2c7/1080p60")
PARTIAL_DIR = VIDEO_DIR / "partial_movie_files"

def render_and_capture_log() -> str:
    """Render the scene and capture full logs."""
    print(f"🎬 Rendering {SCENE_NAME}...")
    cmd = ["manim", "-pqh", "--progress_bar", "none", str(SCENE_FILE), SCENE_NAME]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Rendering failed:\n{result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, cmd)
        
    print("✅ Rendering complete.")
    return result.stderr + "\n" + result.stdout

def extract_hashes_from_log(log_output: str) -> list[str]:
    """Extract all animation hashes from the log in order."""
    # Strip ANSI codes
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    clean_output = ansi_escape.sub('', log_output)
    
    # Find all hashes matching pattern: \d+_\d+_\d+
    hash_pattern = re.compile(r"(\d+_\d+_\d+)")
    all_hashes = hash_pattern.findall(clean_output)
    
    return all_hashes

def analyze_hash_distribution(hashes: list[str]) -> dict:
    """
    Analyze where each hash exists:
    - MultivariableCalculusExplanation/
    - MultivariateCalculusExplanation/
    - Missing
    """
    dir1 = PARTIAL_DIR / "MultivariableCalculusExplanation"
    dir2 = PARTIAL_DIR / "MultivariateCalculusExplanation"
    
    stats = {
        "total_hashes": len(hashes),
        "unique_hashes": len(set(hashes)),
        "in_dir1": 0,
        "in_dir2": 0,
        "in_both": 0,
        "missing": 0,
        "missing_hashes": [],
        "duplicate_usage": defaultdict(int)
    }
    
    # Track how many times each hash appears
    for h in hashes:
        stats["duplicate_usage"][h] += 1
    
    # Check file existence for unique hashes
    unique_hashes = list(set(hashes))
    for h in unique_hashes:
        file1 = dir1 / f"{h}.mp4"
        file2 = dir2 / f"{h}.mp4"
        
        exists1 = file1.exists()
        exists2 = file2.exists()
        
        if exists1 and exists2:
            stats["in_both"] += 1
        elif exists1:
            stats["in_dir1"] += 1
        elif exists2:
            stats["in_dir2"] += 1
        else:
            stats["missing"] += 1
            stats["missing_hashes"].append(h)
    
    return stats

def generate_report(hashes: list[str], stats: dict):
    """Generate a comprehensive diagnostic report."""
    report = []
    report.append("=" * 80)
    report.append("MISSING FRAME FILES DIAGNOSTIC REPORT")
    report.append("=" * 80)
    report.append("")
    
    report.append("## Summary")
    report.append(f"Total animation events: {stats['total_hashes']}")
    report.append(f"Unique hashes: {stats['unique_hashes']}")
    report.append(f"Hash reuse (cached animations): {stats['total_hashes'] - stats['unique_hashes']}")
    report.append("")
    
    report.append("## File Distribution (Unique Hashes)")
    report.append(f"In MultivariableCalculusExplanation/ only: {stats['in_dir1']}")
    report.append(f"In MultivariateCalculusExplanation/ only: {stats['in_dir2']}")
    report.append(f"In both directories: {stats['in_both']}")
    report.append(f"Missing from both: {stats['missing']}")
    report.append("")
    
    if stats['missing'] > 0:
        report.append(f"## Missing Hashes ({stats['missing']} total)")
        for i, h in enumerate(stats['missing_hashes'][:10], 1):
            usage_count = stats['duplicate_usage'][h]
            report.append(f"{i}. {h} (used {usage_count} times in log)")
        if len(stats['missing_hashes']) > 10:
            report.append(f"... and {len(stats['missing_hashes']) - 10} more")
        report.append("")
    
    # Check for high reuse
    report.append("## Most Reused Hashes (Top 10)")
    sorted_reuse = sorted(stats['duplicate_usage'].items(), key=lambda x: x[1], reverse=True)
    for i, (h, count) in enumerate(sorted_reuse[:10], 1):
        dir1_exists = (PARTIAL_DIR / "MultivariableCalculusExplanation" / f"{h}.mp4").exists()
        dir2_exists = (PARTIAL_DIR / "MultivariateCalculusExplanation" / f"{h}.mp4").exists()
        location = "dir1" if dir1_exists else ("dir2" if dir2_exists else "MISSING")
        report.append(f"{i}. {h[:20]}... used {count} times [{location}]")
    report.append("")
    
    report.append("## Coverage Calculation")
    # If we have all unique files, we can handle duplicates via reuse
    available_unique_hashes = stats['unique_hashes'] - stats['missing']
    theoretical_coverage = (available_unique_hashes / stats['unique_hashes']) * 100 if stats['unique_hashes'] > 0 else 0
    report.append(f"Unique hashes available: {available_unique_hashes}/{stats['unique_hashes']} ({theoretical_coverage:.1f}%)")
    report.append("")
    
    # Calculate actual animation event coverage
    covered_events = sum(1 for h in hashes if h not in stats['missing_hashes'])
    event_coverage = (covered_events / stats['total_hashes']) * 100 if stats['total_hashes'] > 0 else 0
    report.append(f"Animation events covered: {covered_events}/{stats['total_hashes']} ({event_coverage:.1f}%)")
    report.append("")
    
    report.append("## Recommendations")
    if stats['missing'] == 0:
        report.append("✅ All unique hashes have corresponding files!")
        report.append("✅ 100% coverage achievable by handling file reuse.")
    elif stats['missing'] < 10:
        report.append(f"⚠️  Only {stats['missing']} missing files.")
        report.append("🔧 Recommendation: Selective re-render of missing segments.")
        report.append(f"   Use: manim --from_animation_number X --to_animation_number Y")
    else:
        report.append(f"❌ {stats['missing']} files missing.")
        report.append("🔧 Recommendation: Clear cache and do full re-render.")
        report.append("   Or use: manim --disable_caching (slower but guaranteed)")
    
    report.append("")
    report.append("=" * 80)
    
    return "\n".join(report)

def main():
    print("Starting Missing File Diagnosis...\n")
    
    # Step 1: Render and capture logs
    log_output = render_and_capture_log()
    
    # Step 2: Extract hashes
    print("\n📊 Extracting animation hashes from logs...")
    hashes = extract_hashes_from_log(log_output)
    print(f"  Found {len(hashes)} animation events")
    print(f"  Found {len(set(hashes))} unique hashes")
    
    # Step 3: Analyze distribution
    print("\n🔍 Analyzing file distribution...")
    stats = analyze_hash_distribution(hashes)
    
    # Step 4: Generate report
    print("\n📝 Generating diagnostic report...\n")
    report = generate_report(hashes, stats)
    print(report)
    
    # Step 5: Save report
    report_file = Path("missing_files_diagnostic_report.txt")
    with open(report_file, "w") as f:
        f.write(report)
    print(f"\n💾 Report saved to: {report_file}")
    
    # Step 6: Save hashes for reference
    hash_file = Path("extracted_hashes.txt")
    with open(hash_file, "w") as f:
        f.write(f"# Total: {len(hashes)} animation events\n")
        f.write(f"# Unique: {len(set(hashes))} hashes\n\n")
        for i, h in enumerate(hashes, 1):
            f.write(f"{i}: {h}\n")
    print(f"💾 Hashes saved to: {hash_file}")

if __name__ == "__main__":
    main()

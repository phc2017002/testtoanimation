"""
Example usage of Manim Video Generation API Client
"""

from api_client import ManimVideoClient, QualityLevel


def example_1_simple():
    """Simple video generation example"""
    print("=== Example 1: Simple Video Generation ===\n")
    
    client = ManimVideoClient()
    
    # Create video
    job = client.create_video(
        prompt="Create a 30-second animation explaining the concept of recursion using a simple example",
        quality=QualityLevel.LOW  # Use low quality for quick testing
    )
    
    print(f"Job ID: {job['job_id']}")
    print(f"Status: {job['status']}")
    
    return job['job_id']


def example_2_with_progress():
    """Video generation with progress tracking"""
    print("\n=== Example 2: With Progress Tracking ===\n")
    
    client = ManimVideoClient()
    
    # Progress callback
    def show_progress(status):
        stage = status['progress']['stage']
        percentage = status['progress']['percentage']
        message = status['progress']['message']
        print(f"[{percentage:3d}%] {stage}: {message}")
    
    # Create and wait
    job = client.create_video(
        prompt="""
        Create a 1-minute animation visualizing bubble sort algorithm:
        - Show an array of random numbers
        - Animate the comparison and swapping process
        - Highlight elements being compared
        - Show sorted portion in green
        """,
        quality=QualityLevel.LOW
    )
    
    print(f"Job created: {job['job_id']}\n")
    
    # Wait for completion with progress updates
    result = client.wait_for_completion(
        job['job_id'],
        poll_interval=3,
        callback=show_progress
    )
    
    if result['status'] == 'completed':
        print(f"\n✓ Video completed!")
        print(f"  Duration: {result.get('duration', 'N/A')}s")
        print(f"  Download URL: {result.get('video_url')}")
    else:
        print(f"\n✗ Failed: {result.get('error')}")
    
    return job['job_id']


def example_3_complete_workflow():
    """Complete workflow: create, wait, download"""
    print("\n=== Example 3: Complete Workflow ===\n")
    
    client = ManimVideoClient()
    
    def progress(status):
        pct = status['progress']['percentage']
        msg = status['progress']['message']
        print(f"[{pct:3d}%] {msg}")
    
    # One-shot: create, wait, and download
    result = client.generate_and_download(
        prompt="""
        Create a 45-second animation about binary search:
        - Show a sorted array
        - Animate the search process
        - Highlight the middle element
        - Show elimination of half the array each time
        """,
        output_path="binary_search_animation.mp4",
        quality=QualityLevel.LOW,
        progress_callback=progress
    )
    
    print(f"\n✓ Success!")
    print(f"  File: binary_search_animation.mp4")
    print(f"  Duration: {result.get('duration')}s")


def example_4_list_jobs():
    """List all jobs"""
    print("\n=== Example 4: List All Jobs ===\n")
    
    client = ManimVideoClient()
    
    jobs = client.list_jobs(limit=10)
    
    print(f"Total jobs: {jobs['total']}\n")
    
    for job in jobs['jobs'][:5]:  # Show first 5
        print(f"Job: {job['job_id']}")
        print(f"  Status: {job['status']}")
        print(f"  Created: {job['created_at']}")
        if job.get('progress'):
            print(f"  Progress: {job['progress']['percentage']}%")
        print()


def example_5_health_check():
    """Check API health"""
    print("\n=== Example 5: Health Check ===\n")
    
    client = ManimVideoClient()
    
    health = client.health_check()
    
    print(f"Status: {health['status']}")
    print(f"Timestamp: {health['timestamp']}")
    print(f"\nJob Statistics:")
    print(f"  Total: {health['jobs']['total']}")
    print(f"  Pending: {health['jobs']['pending']}")
    print(f"  Processing: {health['jobs']['processing']}")
    print(f"  Completed: {health['jobs']['completed']}")
    print(f"  Failed: {health['jobs']['failed']}")


if __name__ == "__main__":
    import sys
    
    print("Manim Video Generation API - Client Examples")
    print("=" * 60)
    
    # Check if server is running
    try:
        client = ManimVideoClient()
        client.health_check()
        print("✓ API server is running\n")
    except Exception as e:
        print(f"✗ Error: Cannot connect to API server")
        print(f"  Make sure the server is running: poetry run python api_server.py")
        sys.exit(1)
    
    # Run examples
    print("\nChoose an example to run:")
    print("1. Simple video generation")
    print("2. Video generation with progress tracking")
    print("3. Complete workflow (create + wait + download)")
    print("4. List all jobs")
    print("5. Health check")
    print("0. Run all examples")
    
    choice = input("\nEnter choice (0-5): ").strip()
    
    examples = {
        "1": example_1_simple,
        "2": example_2_with_progress,
        "3": example_3_complete_workflow,
        "4": example_4_list_jobs,
        "5": example_5_health_check,
    }
    
    if choice == "0":
        for func in examples.values():
            func()
            print("\n" + "-" * 60)
    elif choice in examples:
        examples[choice]()
    else:
        print("Invalid choice")

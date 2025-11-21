"""
Python client library for Manim Video Generation API
"""

import requests
import time
from typing import Optional, Dict, Any
from enum import Enum


class QualityLevel(str, Enum):
    """Video quality levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    ULTRA = "ultra"


class JobStatus(str, Enum):
    """Job status"""
    PENDING = "pending"
    GENERATING_CODE = "generating_code"
    RENDERING = "rendering"
    COMPLETED = "completed"
    FAILED = "failed"


class ManimVideoClient:
    """Client for Manim Video Generation API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        Initialize client
        
        Args:
            base_url: Base URL of the API server
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
    
    def create_video(
        self,
        prompt: str,
        quality: QualityLevel = QualityLevel.HIGH,
        scene_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new video generation job
        
        Args:
            prompt: Detailed animation prompt
            quality: Video quality level
            scene_name: Optional custom scene name
        
        Returns:
            Job information including job_id
        
        Example:
            >>> client = ManimVideoClient()
            >>> job = client.create_video(
            ...     prompt="Explain bubble sort with animations",
            ...     quality=QualityLevel.HIGH
            ... )
            >>> print(job['job_id'])
        """
        response = self.session.post(
            f"{self.base_url}/api/videos",
            json={
                "prompt": prompt,
                "quality": quality.value,
                "scene_name": scene_name
            }
        )
        response.raise_for_status()
        return response.json()
    
    def get_status(self, job_id: str) -> Dict[str, Any]:
        """
        Get job status
        
        Args:
            job_id: Job ID returned from create_video()
        
        Returns:
            Job status information
        
        Example:
            >>> status = client.get_status(job_id)
            >>> print(status['status'])
            >>> print(status['progress']['percentage'])
        """
        response = self.session.get(f"{self.base_url}/api/jobs/{job_id}")
        response.raise_for_status()
        return response.json()
    
    def wait_for_completion(
        self,
        job_id: str,
        poll_interval: int = 5,
        timeout: Optional[int] = None,
        callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """
        Wait for job to complete
        
        Args:
            job_id: Job ID
            poll_interval: Seconds between status checks
            timeout: Maximum seconds to wait (None = no timeout)
            callback: Optional function called with status on each poll
        
        Returns:
            Final job status
        
        Example:
            >>> def progress_callback(status):
            ...     print(f"{status['progress']['percentage']}%: {status['progress']['message']}")
            >>> 
            >>> result = client.wait_for_completion(
            ...     job_id,
            ...     callback=progress_callback
            ... )
        """
        start_time = time.time()
        
        while True:
            status = self.get_status(job_id)
            
            if callback:
                callback(status)
            
            if status['status'] in [JobStatus.COMPLETED, JobStatus.FAILED]:
                return status
            
            if timeout and (time.time() - start_time > timeout):
                raise TimeoutError(f"Job did not complete within {timeout} seconds")
            
            time.sleep(poll_interval)
    
    def download_video(self, job_id: str, output_path: str) -> str:
        """
        Download completed video
        
        Args:
            job_id: Job ID
            output_path: Path to save video file
        
        Returns:
            Path to downloaded file
        
        Example:
            >>> client.download_video(job_id, "my_animation.mp4")
            'my_animation.mp4'
        """
        response = self.session.get(
            f"{self.base_url}/api/videos/{job_id}",
            stream=True
        )
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return output_path
    
    def list_jobs(self, limit: int = 50) -> Dict[str, Any]:
        """
        List all jobs
        
        Args:
            limit: Maximum number of jobs to return
        
        Returns:
            Dictionary with job list
        
        Example:
            >>> jobs = client.list_jobs(limit=10)
            >>> for job in jobs['jobs']:
            ...     print(f"{job['job_id']}: {job['status']}")
        """
        response = self.session.get(
            f"{self.base_url}/api/jobs",
            params={"limit": limit}
        )
        response.raise_for_status()
        return response.json()
    
    def delete_job(self, job_id: str) -> Dict[str, Any]:
        """
        Delete a job and its files
        
        Args:
            job_id: Job ID
        
        Returns:
            Deletion confirmation
        
        Example:
            >>> client.delete_job(job_id)
            {'message': 'Job deleted successfully', 'job_id': '...'}
        """
        response = self.session.delete(f"{self.base_url}/api/jobs/{job_id}")
        response.raise_for_status()
        return response.json()
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check API health
        
        Returns:
            Health status and statistics
        
        Example:
            >>> health = client.health_check()
            >>> print(f"Total jobs: {health['jobs']['total']}")
        """
        response = self.session.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()
    
    def generate_and_download(
        self,
        prompt: str,
        output_path: str,
        quality: QualityLevel = QualityLevel.HIGH,
        poll_interval: int = 5,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """
        Complete workflow: create, wait, and download
        
        Args:
            prompt: Animation prompt
            output_path: Where to save video
            quality: Video quality
            poll_interval: Status check interval
            progress_callback: Optional progress callback
        
        Returns:
            Final job status
        
        Example:
            >>> def show_progress(status):
            ...     pct = status['progress']['percentage']
            ...     msg = status['progress']['message']
            ...     print(f"[{pct}%] {msg}")
            >>> 
            >>> client.generate_and_download(
            ...     prompt="Explain merge sort",
            ...     output_path="merge_sort.mp4",
            ...     progress_callback=show_progress
            ... )
        """
        # Create job
        job = self.create_video(prompt, quality)
        job_id = job['job_id']
        
        print(f"✓ Job created: {job_id}")
        
        # Wait for completion
        result = self.wait_for_completion(
            job_id,
            poll_interval=poll_interval,
            callback=progress_callback
        )
        
        if result['status'] == JobStatus.COMPLETED:
            # Download video
            self.download_video(job_id, output_path)
            print(f"✓ Video downloaded: {output_path}")
            return result
        else:
            raise Exception(f"Job failed: {result.get('error', 'Unknown error')}")


# ============================================================================
# CLI Tool
# ============================================================================

def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Manim Video Generation API Client"
    )
    parser.add_argument(
        "command",
        choices=["create", "status", "download", "list", "generate"],
        help="Command to execute"
    )
    parser.add_argument("--prompt", help="Animation prompt")
    parser.add_argument("--job-id", help="Job ID")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument(
        "--quality",
        choices=["low", "medium", "high", "ultra"],
        default="high",
        help="Video quality"
    )
    parser.add_argument(
        "--url",
        default="http://localhost:8000",
        help="API base URL"
    )
    
    args = parser.parse_args()
    client = ManimVideoClient(args.url)
    
    if args.command == "create":
        if not args.prompt:
            print("Error: --prompt required")
            return
        
        job = client.create_video(args.prompt, QualityLevel(args.quality))
        print(f"Job created: {job['job_id']}")
        print(f"Status: {job['status']}")
    
    elif args.command == "status":
        if not args.job_id:
            print("Error: --job-id required")
            return
        
        status = client.get_status(args.job_id)
        print(f"Job ID: {status['job_id']}")
        print(f"Status: {status['status']}")
        print(f"Progress: {status['progress']['percentage']}%")
        print(f"Message: {status['progress']['message']}")
    
    elif args.command == "download":
        if not args.job_id or not args.output:
            print("Error: --job-id and --output required")
            return
        
        path = client.download_video(args.job_id, args.output)
        print(f"Downloaded: {path}")
    
    elif args.command == "list":
        jobs = client.list_jobs()
        print(f"Total jobs: {jobs['total']}")
        for job in jobs['jobs']:
            print(f"  {job['job_id']}: {job['status']}")
    
    elif args.command == "generate":
        if not args.prompt or not args.output:
            print("Error: --prompt and --output required")
            return
        
        def progress(status):
            pct = status['progress']['percentage']
            msg = status['progress']['message']
            print(f"[{pct:3d}%] {msg}")
        
        client.generate_and_download(
            args.prompt,
            args.output,
            QualityLevel(args.quality),
            progress_callback=progress
        )


if __name__ == "__main__":
    main()

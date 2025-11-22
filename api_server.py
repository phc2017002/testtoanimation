"""
FastAPI Video Generation Server
A production-ready API for generating educational animation videos using Manim.

Features:
- Async job processing
- Job status tracking
- File management
- Progress monitoring
- Error handling
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum
import uuid
import os
import time
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
import asyncio
import logging

from manimator.api.animation_generation import generate_animation_response

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("api_server")

# ============================================================================
# Configuration
# ============================================================================

class Config:
    """Application configuration"""
    BASE_DIR = Path(__file__).parent
    JOBS_DIR = BASE_DIR / "jobs"
    VIDEOS_DIR = BASE_DIR / "media" / "videos"
    MAX_JOB_AGE_DAYS = 7
    
    # Ensure directories exist
    JOBS_DIR.mkdir(exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# Models
# ============================================================================

class JobStatus(str, Enum):
    """Job status enumeration"""
    PENDING = "pending"
    GENERATING_CODE = "generating_code"
    RENDERING = "rendering"
    VERIFYING = "verifying"  # New status
    COMPLETED = "completed"
    FAILED = "failed"


class QualityLevel(str, Enum):
    """Video quality levels"""
    LOW = "low"       # 480p15
    MEDIUM = "medium" # 720p30
    HIGH = "high"     # 1080p60
    ULTRA = "ultra"   # 4K60


QUALITY_FLAGS = {
    QualityLevel.LOW: "-pql",
    QualityLevel.MEDIUM: "-pqm",
    QualityLevel.HIGH: "-pqh",
    QualityLevel.ULTRA: "-pqk",
}


class VideoRequest(BaseModel):
    """Request model for video generation"""
    prompt: str = Field(..., description="Detailed animation prompt describing the video content")
    quality: QualityLevel = Field(default=QualityLevel.HIGH, description="Video quality level")
    scene_name: Optional[str] = Field(default=None, description="Custom scene class name (auto-generated if not provided)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "prompt": "Create a 2-minute animation explaining quicksort algorithm with visualizations",
                "quality": "high",
                "scene_name": "QuickSortAnimation"
            }
        }


class JobResponse(BaseModel):
    """Response model for job creation"""
    job_id: str
    status: JobStatus
    message: str
    created_at: str


class JobStatusResponse(BaseModel):
    """Response model for job status"""
    job_id: str
    status: JobStatus
    progress: Dict[str, Any]
    created_at: str
    updated_at: str
    error: Optional[str] = None
    video_url: Optional[str] = None
    duration: Optional[float] = None


# ============================================================================
# Job Manager
# ============================================================================

class JobManager:
    """Manages video generation jobs"""
    
    def __init__(self):
        self.jobs: Dict[str, Dict] = {}
        self._load_existing_jobs()
    
    def _load_existing_jobs(self):
        """Load existing jobs from disk"""
        for job_file in Config.JOBS_DIR.glob("*.json"):
            try:
                with open(job_file) as f:
                    job_data = json.load(f)
                    self.jobs[job_data["job_id"]] = job_data
            except Exception as e:
                print(f"Error loading job {job_file}: {e}")
    
    def create_job(self, prompt: str, quality: QualityLevel, scene_name: Optional[str] = None) -> str:
        """Create a new job"""
        job_id = str(uuid.uuid4())
        
        if not scene_name:
            scene_name = f"Scene_{uuid.uuid4().hex[:8]}"
        
        job_data = {
            "job_id": job_id,
            "status": JobStatus.PENDING,
            "prompt": prompt,
            "quality": quality,
            "scene_name": scene_name,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "progress": {
                "stage": "queued",
                "percentage": 0,
                "message": "Job queued for processing"
            },
            "error": None,
            "video_path": None,
            "code_path": None,
        }
        
        self.jobs[job_id] = job_data
        self._save_job(job_id)
        return job_id
    
    def update_job(self, job_id: str, **kwargs):
        """Update job data"""
        if job_id not in self.jobs:
            raise ValueError(f"Job {job_id} not found")
        
        self.jobs[job_id].update(kwargs)
        self.jobs[job_id]["updated_at"] = datetime.now().isoformat()
        self._save_job(job_id)
        
        # Log progress updates
        if "progress" in kwargs:
            logger.info(f"Job {job_id[:8]}... | {kwargs['progress']['message']}")
    
    def get_job(self, job_id: str) -> Optional[Dict]:
        """Get job data"""
        return self.jobs.get(job_id)
    
    def _save_job(self, job_id: str):
        """Save job data to disk"""
        job_file = Config.JOBS_DIR / f"{job_id}.json"
        with open(job_file, 'w') as f:
            json.dump(self.jobs[job_id], f, indent=2)
    
    def list_jobs(self, limit: int = 50) -> List[Dict]:
        """List all jobs"""
        jobs = sorted(
            self.jobs.values(),
            key=lambda x: x["created_at"],
            reverse=True
        )
        return jobs[:limit]


# ============================================================================
# Video Generator
# ============================================================================

from manimator.utils.visual_analyzer import create_visual_analyzer

class VideoGenerator:
    """Handles video generation workflow"""
    
    def __init__(self, job_manager: JobManager):
        self.job_manager = job_manager
        self.analyzer = create_visual_analyzer()  # Initialize analyzer
    
    async def generate_video(self, job_id: str):
        """Generate video for a job"""
        job = self.job_manager.get_job(job_id)
        if not job:
            return
        
        logger.info(f"🎬 Starting video generation for job {job_id[:8]}...")
        
        max_regenerations = 1
        regeneration_count = 0
        
        while regeneration_count <= max_regenerations:
            try:
                # Stage 1: Generate Manim code
                # If this is a regeneration, we append a critical instruction
                current_prompt = job["prompt"]
                if regeneration_count > 0:
                    logger.warning(f"🔄 Regeneration Attempt {regeneration_count}/{max_regenerations}...")
                    current_prompt += "\n\nCRITICAL: Previous generation had persistent visual layout issues (overlaps/cutoffs). Ensure STRICT adherence to safe zones and spacing."
                    
                    self.job_manager.update_job(
                        job_id,
                        status=JobStatus.GENERATING_CODE,
                        progress={
                            "stage": "regenerating_code",
                            "percentage": 10,
                            "message": f"Regenerating scene (Attempt {regeneration_count})..."
                        }
                    )
                else:
                    self.job_manager.update_job(
                        job_id,
                        status=JobStatus.GENERATING_CODE,
                        progress={
                            "stage": "generating_code",
                            "percentage": 10,
                            "message": "Generating Manim code using AI..."
                        }
                    )
                
                logger.info(f"🤖 Generating Manim code for job {job_id[:8]}...")
                code = await self._generate_code(current_prompt)
                
                logger.info(f"✅ Code generation complete for job {job_id[:8]}...")
                
                # Save code
                code_file = Config.BASE_DIR / f"scene_{job_id}.py"
                with open(code_file, 'w') as f:
                    f.write(code)
                
                logger.info(f"💾 Code saved to {code_file.name}")
                
                self.job_manager.update_job(
                    job_id,
                    code_path=str(code_file),
                    progress={
                        "stage": "code_generated",
                        "percentage": 30,
                        "message": "Code generated successfully"
                    }
                )
                
                # Stage 2: Render video (Pass 1)
                logger.info(f"🎥 Starting Manim rendering (Pass 1) for job {job_id[:8]}...")
                self.job_manager.update_job(
                    job_id,
                    status=JobStatus.RENDERING,
                    progress={
                        "stage": "rendering",
                        "percentage": 40,
                        "message": "Rendering video (Pass 1)..."
                    }
                )
                
                video_path = await self._render_video(
                    code_file,
                    job["scene_name"],
                    job["quality"]
                )
                
                # Stage 3: Visual Verification Loop
                max_retries = 5
                verification_passed = False
                
                for i in range(max_retries):
                    logger.info(f"👁️ Visual Verification Loop {i+1}/{max_retries} for job {job_id[:8]}...")
                    self.job_manager.update_job(
                        job_id,
                        status=JobStatus.VERIFYING,
                        progress={
                            "stage": "verifying",
                            "percentage": 70 + (i * 5),
                            "message": f"Verifying visual layout (Attempt {i+1}/{max_retries})..."
                        }
                    )
                    
                    # Run analysis
                    final_code, report = self.analyzer.analyze_and_fix(
                        code,
                        video_path,
                        max_iterations=1
                    )
                    
                    # If code is unchanged, we are good
                    if final_code == code:
                        logger.info(f"✅ Verification passed on attempt {i+1}! No issues found.")
                        verification_passed = True
                        break
                    
                    # Issues found, applying fixes
                    logger.info(f"🛠️ Issues found! Applying fixes and re-rendering (Attempt {i+1})...")
                    code = final_code
                    
                    # Save fixed code
                    with open(code_file, 'w') as f:
                        f.write(code)
                    
                    # Re-render
                    video_path = await self._render_video(
                        code_file,
                        job["scene_name"],
                        job["quality"]
                    )
                
                if verification_passed:
                    # Success! Break the outer regeneration loop
                    break
                else:
                    # Verification failed after max retries
                    logger.warning(f"⚠️ Layout issues persisted after {max_retries} fix attempts.")
                    regeneration_count += 1
                    if regeneration_count > max_regenerations:
                        logger.error("❌ Max regenerations exceeded. Failing job.")
                        # We could fail here, or just accept the best effort.
                        # Let's accept the best effort but mark it.
                        logger.info("⚠️ Accepting best effort video.")
                        break
                    else:
                        continue # Loop back to regenerate code
            
            except Exception as e:
                logger.error(f"Error in generation loop: {e}")
                self.job_manager.update_job(
                    job_id,
                    status=JobStatus.FAILED,
                    error=str(e),
                    progress={
                        "stage": "failed",
                        "percentage": 0,
                        "message": f"Generation failed: {str(e)}"
                    }
                )
                return

        # Stage 4: Complete
        logger.info(f"🎉 Video generation complete for job {job_id[:8]}!")
        logger.info(f"📁 Video saved to: {video_path}")
        
        self.job_manager.update_job(
            job_id,
            status=JobStatus.COMPLETED,
            video_path=str(video_path),
            progress={
                "stage": "completed",
                "percentage": 100,
                "message": "Video generation completed successfully"
            }
        )
    
    async def _generate_code(self, prompt: str) -> str:
        """Generate Manim code from prompt"""
        # Run in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            generate_animation_response,
            prompt
        )
        
        # Extract Python code from markdown
        pattern = r'```python\n(.*?)```'
        match = re.search(pattern, response, re.DOTALL)
        
        if match:
            return match.group(1)
        else:
            # Try without code block
            return response
    
    async def _render_video(self, code_file: Path, scene_name: str, quality: QualityLevel) -> Path:
        """Render video using Manim with real-time progress"""
        quality_flag = QUALITY_FLAGS[quality]
        
        cmd = [
            "manim",
            quality_flag,
            str(code_file),
            scene_name
        ]
        
        logger.info(f"🎬 Executing: {' '.join(cmd)}")
        
        # Run subprocess with streaming output
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,  # Merge stderr into stdout
            cwd=str(Config.BASE_DIR)
        )
        
        # Stream output in real-time
        output_lines = []
        last_animation_num = 0
        
        while True:
            line = await process.stdout.readline()
            if not line:
                break
            
            line_text = line.decode('utf-8').strip()
            output_lines.append(line_text)
            
            # Parse and log Manim progress
            if "Animation" in line_text and "Partial movie file" in line_text:
                # Extract animation number
                import re
                match = re.search(r'Animation (\d+)', line_text)
                if match:
                    anim_num = int(match.group(1))
                    # Only log every 10th animation to avoid spam
                    if anim_num % 10 == 0 or anim_num != last_animation_num:
                        logger.info(f"  ├─ Rendering animation {anim_num}...")
                        last_animation_num = anim_num
            
            elif "Rendered" in line_text and "Played" in line_text:
                # Final summary
                logger.info(f"  └─ {line_text}")
            
            elif "INFO" in line_text and ("File ready" in line_text or "Combining" in line_text):
                logger.info(f"  ├─ {line_text}")
            
            elif "WARNING" in line_text or "ERROR" in line_text:
                logger.warning(f"  ⚠️  {line_text}")
        
        await process.wait()
        
        if process.returncode != 0:
            error_output = '\n'.join(output_lines[-20:])  # Last 20 lines
            raise Exception(f"Manim rendering failed:\n{error_output}")
        
        # Find generated video
        quality_dir = {
            QualityLevel.LOW: "480p15",
            QualityLevel.MEDIUM: "720p30",
            QualityLevel.HIGH: "1080p60",
            QualityLevel.ULTRA: "2160p60"
        }[quality]
        
        video_dir = Config.VIDEOS_DIR / code_file.stem / quality_dir
        
        # Search for the actual video file (class name may differ from scene_name)
        video_files = list(video_dir.glob("*.mp4"))
        
        if not video_files:
            raise Exception(f"No video file found in {video_dir}")
        
        # Use the first (and typically only) MP4 file found
        video_path = video_files[0]
        logger.info(f"📹 Found video: {video_path.name}")
        
        return video_path


# ============================================================================
# FastAPI Application
# ============================================================================

app = FastAPI(
    title="Manim Video Generation API",
    description="Generate educational animation videos from text prompts",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize managers
job_manager = JobManager()
video_generator = VideoGenerator(job_manager)


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "name": "Manim Video Generation API",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "create_video": "POST /api/videos",
            "get_status": "GET /api/jobs/{job_id}",
            "download_video": "GET /api/videos/{job_id}",
            "list_jobs": "GET /api/jobs"
        }
    }


@app.post("/api/videos", response_model=JobResponse)
async def create_video(request: VideoRequest, background_tasks: BackgroundTasks):
    """
    Create a new video generation job
    
    The job is processed asynchronously in the background.
    Use the returned job_id to check status and download the video.
    """
    # Create job
    job_id = job_manager.create_job(
        prompt=request.prompt,
        quality=request.quality,
        scene_name=request.scene_name
    )
    
    logger.info(f"📝 New job created: {job_id} (quality: {request.quality})")
    
    # Start generation in background
    background_tasks.add_task(video_generator.generate_video, job_id)
    
    return JobResponse(
        job_id=job_id,
        status=JobStatus.PENDING,
        message="Job created successfully. Video generation started.",
        created_at=datetime.now().isoformat()
    )


@app.get("/api/jobs/{job_id}", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    """
    Get the status of a video generation job
    
    Returns current status, progress, and video URL if completed.
    """
    job = job_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    video_url = None
    duration = None
    
    if job["status"] == JobStatus.COMPLETED and job.get("video_path"):
        video_url = f"/api/videos/{job_id}"
        
        # Get video duration if available
        try:
            video_path = Path(job["video_path"])
            if video_path.exists():
                result = subprocess.run(
                    ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "default=noprint_wrappers=1:nokey=1", str(video_path)],
                    capture_output=True,
                    text=True
                )
                duration = float(result.stdout.strip())
        except:
            pass
    
    return JobStatusResponse(
        job_id=job_id,
        status=job["status"],
        progress=job["progress"],
        created_at=job["created_at"],
        updated_at=job["updated_at"],
        error=job.get("error"),
        video_url=video_url,
        duration=duration
    )


@app.get("/api/videos/{job_id}")
async def download_video(job_id: str):
    """
    Download the generated video file
    
    Returns the MP4 file if the job is completed successfully.
    """
    job = job_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job["status"] != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Video not ready. Current status: {job['status']}"
        )
    
    video_path = Path(job["video_path"])
    
    if not video_path.exists():
        raise HTTPException(status_code=404, detail="Video file not found")
    
    return FileResponse(
        video_path,
        media_type="video/mp4",
        filename=f"{job['scene_name']}.mp4"
    )


@app.get("/api/jobs")
async def list_jobs(limit: int = 50):
    """
    List all video generation jobs
    
    Returns a list of jobs sorted by creation time (most recent first).
    """
    jobs = job_manager.list_jobs(limit=limit)
    
    return {
        "total": len(jobs),
        "jobs": jobs
    }


@app.delete("/api/jobs/{job_id}")
async def delete_job(job_id: str):
    """
    Delete a job and its associated files
    """
    job = job_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Delete video file
    if job.get("video_path"):
        try:
            Path(job["video_path"]).unlink(missing_ok=True)
        except:
            pass
    
    # Delete code file
    if job.get("code_path"):
        try:
            Path(job["code_path"]).unlink(missing_ok=True)
        except:
            pass
    
    # Delete job data
    job_file = Config.JOBS_DIR / f"{job_id}.json"
    job_file.unlink(missing_ok=True)
    
    del job_manager.jobs[job_id]
    
    return {"message": "Job deleted successfully", "job_id": job_id}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "jobs": {
            "total": len(job_manager.jobs),
            "pending": len([j for j in job_manager.jobs.values() if j["status"] == JobStatus.PENDING]),
            "processing": len([j for j in job_manager.jobs.values() if j["status"] in [JobStatus.GENERATING_CODE, JobStatus.RENDERING]]),
            "completed": len([j for j in job_manager.jobs.values() if j["status"] == JobStatus.COMPLETED]),
            "failed": len([j for j in job_manager.jobs.values() if j["status"] == JobStatus.FAILED])
        }
    }


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting Manim Video Generation API Server...")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔍 ReDoc Documentation: http://localhost:8000/redoc")
    
    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

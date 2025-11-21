"""
FastAPI 3D Video Generation Server

A production-ready API for generating 3D educational animation videos using Manim's ThreeDScene.
Supports all STEM visualizations: mathematical, scientific, geometric, and data visualization.

Server runs on port 8001 (2D server on 8000)
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum
import uuid
import os
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
import asyncio
import logging

from manimator.threed.api.animation_generation_3d import (
    generate_3d_animation_response,
    generate_3d_animation_with_category
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("api_server_3d")

# ============================================================================
# Configuration
# ============================================================================

class Config:
    """Application configuration"""
    BASE_DIR = Path(__file__).parent
    JOBS_DIR = BASE_DIR / "jobs_3d"
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
    COMPLETED = "completed"
    FAILED = "failed"


class QualityLevel(str, Enum):
    """Video quality levels"""
    LOW = "low"       # 480p15
    MEDIUM = "medium" # 720p30
    HIGH = "high"     # 1080p60
    ULTRA = "ultra"   # 4K60


class STEMCategory(str, Enum):
    """STEM visualization categories"""
    MATHEMATICAL = "mathematical"  # Surfaces, vector fields, calculus
    SCIENTIFIC = "scientific"      # Molecules, physics, simulations
    GEOMETRIC = "geometric"        # Shapes, transformations
    DATA = "data"                  # 3D data visualization
    GENERAL = "general"            # Mixed or unspecified


QUALITY_FLAGS = {
    QualityLevel.LOW: "-pql",
    QualityLevel.MEDIUM: "-pqm",
    QualityLevel.HIGH: "-pqh",
    QualityLevel.ULTRA: "-pqk",
}


class Video3DRequest(BaseModel):
    """Request model for 3D video generation"""
    prompt: str = Field(..., description="Detailed 3D animation prompt")
    quality: QualityLevel = Field(default=QualityLevel.HIGH, description="Video quality level")
    category: STEMCategory = Field(default=STEMCategory.GENERAL, description="STEM visualization category")
    scene_name: Optional[str] = Field(default=None, description="Custom scene class name")
    
    class Config:
        json_schema_extra = {
            "example": {
                "prompt": "Create a 3D animation showing a rotating DNA double helix with labeled base pairs",
                "quality": "high",
                "category": "scientific",
                "scene_name": "DNAHelix"
            }
        }


class JobResponse(BaseModel):
    """Response model for job creation"""
    job_id: str
    status: JobStatus
    message: str
    category: STEMCategory
    created_at: str


class JobStatusResponse(BaseModel):
    """Response model for job status"""
    job_id: str
    status: JobStatus
    category: STEMCategory
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
    """Manages 3D video generation jobs"""
    
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
                logger.error(f"Error loading job {job_file}: {e}")
    
    def create_job(
        self,
        prompt: str,
        quality: QualityLevel,
        category: STEMCategory,
        scene_name: Optional[str] = None
    ) -> str:
        """Create a new job"""
        job_id = str(uuid.uuid4())
        
        if not scene_name:
            scene_name = f"Scene3D_{uuid.uuid4().hex[:8]}"
        
        job_data = {
            "job_id": job_id,
            "status": JobStatus.PENDING,
            "prompt": prompt,
            "quality": quality,
            "category": category,
            "scene_name": scene_name,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "progress": {
                "stage": "queued",
                "percentage": 0,
                "message": "3D animation job queued for processing"
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
            logger.info(f"3D Job {job_id[:8]}... | {kwargs['progress']['message']}")
    
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

class VideoGenerator3D:
    """Handles 3D video generation workflow"""
    
    def __init__(self, job_manager: JobManager):
        self.job_manager = job_manager
    
    async def generate_video(self, job_id: str):
        """Generate 3D video for a job"""
        job = self.job_manager.get_job(job_id)
        if not job:
            return
        
        logger.info(f"🎬 Starting 3D video generation for job {job_id[:8]}... (Category: {job['category']})")
        
        try:
            # Stage 1: Generate Manim 3D code
            logger.info(f"🤖 Generating 3D Manim code for job {job_id[:8]}...")
            self.job_manager.update_job(
                job_id,
                status=JobStatus.GENERATING_CODE,
                progress={
                    "stage": "generating_code",
                    "percentage": 10,
                    "message": "Generating 3D Manim code using AI..."
                }
            )
            
            code = await self._generate_code(job["prompt"], job["category"])
            
            logger.info(f"✅ 3D code generation complete for job {job_id[:8]}...")
            
            # Save code
            code_file = Config.BASE_DIR / f"scene_3d_{job_id}.py"
            with open(code_file, 'w') as f:
                f.write(code)
            
            logger.info(f"💾 Code saved to {code_file.name}")
            
            self.job_manager.update_job(
                job_id,
                code_path=str(code_file),
                progress={
                    "stage": "code_generated",
                    "percentage": 30,
                    "message": "3D code generated successfully"
                }
            )
            
            # Stage 2: Render 3D video
            logger.info(f"🎥 Starting 3D Manim rendering for job {job_id[:8]}... (this may take several minutes)")
            self.job_manager.update_job(
                job_id,
                status=JobStatus.RENDERING,
                progress={
                    "stage": "rendering",
                    "percentage": 40,
                    "message": "Rendering 3D video with Manim..."
                }
            )
            
            video_path = await self._render_video(
                code_file,
                job["scene_name"],
                job["quality"]
            )
            
            # Stage 3: Complete
            logger.info(f"🎉 3D video rendering complete for job {job_id[:8]}!")
            logger.info(f"📁 Video saved to: {video_path}")
            
            self.job_manager.update_job(
                job_id,
                status=JobStatus.COMPLETED,
                video_path=str(video_path),
                progress={
                    "stage": "completed",
                    "percentage": 100,
                    "message": "3D video generation completed successfully"
                }
            )
            
        except Exception as e:
            logger.error(f"❌ 3D Job {job_id[:8]}... failed: {str(e)}")
            self.job_manager.update_job(
                job_id,
                status=JobStatus.FAILED,
                error=str(e),
                progress={
                    "stage": "failed",
                    "percentage": 0,
                    "message": f"Error: {str(e)}"
                }
            )
    
    async def _generate_code(self, prompt: str, category: STEMCategory) -> str:
        """Generate 3D Manim code from prompt"""
        loop = asyncio.get_event_loop()
        
        if category != STEMCategory.GENERAL:
            response = await loop.run_in_executor(
                None,
                generate_3d_animation_with_category,
                prompt,
                category
            )
        else:
            response = await loop.run_in_executor(
                None,
                generate_3d_animation_response,
                prompt
            )
        
        # Extract Python code from markdown
        pattern = r'```python\n(.*?)```'
        match = re.search(pattern, response, re.DOTALL)
        
        if match:
            return match.group(1)
        else:
            return response
    
    async def _render_video(self, code_file: Path, scene_name: str, quality: QualityLevel) -> Path:
        """Render 3D video using Manim with real-time progress"""
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
            stderr=asyncio.subprocess.STDOUT,
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
                import re
                match = re.search(r'Animation (\d+)', line_text)
                if match:
                    anim_num = int(match.group(1))
                    if anim_num % 10 == 0 or anim_num != last_animation_num:
                        logger.info(f"  ├─ Rendering 3D animation {anim_num}...")
                        last_animation_num = anim_num
            
            elif "Rendered" in line_text and "Played" in line_text:
                logger.info(f"  └─ {line_text}")
            
            elif "INFO" in line_text and ("File ready" in line_text or "Combining" in line_text):
                logger.info(f"  ├─ {line_text}")
            
            elif "WARNING" in line_text or "ERROR" in line_text:
                logger.warning(f"  ⚠️  {line_text}")
        
        await process.wait()
        
        if process.returncode != 0:
            error_output = '\n'.join(output_lines[-20:])
            raise Exception(f"3D Manim rendering failed:\n{error_output}")
        
        # Find generated video
        quality_dir = {
            QualityLevel.LOW: "480p15",
            QualityLevel.MEDIUM: "720p30",
            QualityLevel.HIGH: "1080p60",
            QualityLevel.ULTRA: "2160p60"
        }[quality]
        
        video_dir = Config.VIDEOS_DIR / code_file.stem / quality_dir
        video_path = video_dir / f"{scene_name}.mp4"
        
        if not video_path.exists():
            raise Exception(f"3D video file not found at {video_path}")
        
        return video_path


# ============================================================================
# FastAPI Application
# ============================================================================

app = FastAPI(
    title="Manim 3D Video Generation API",
    description="Generate educational 3D animation videos from text prompts - STEM visualizations",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize managers
job_manager = JobManager()
video_generator = VideoGenerator3D(job_manager)


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "name": "Manim 3D Video Generation API",
        "version": "1.0.0",
        "description": "STEM 3D Visualizations",
        "categories": ["mathematical", "scientific", "geometric", "data"],
        "endpoints": {
            "docs": "/docs",
            "create_3d_video": "POST /api/3d-videos",
            "get_status": "GET /api/3d-jobs/{job_id}",
            "download_video": "GET /api/3d-videos/{job_id}",
            "list_jobs": "GET /api/3d-jobs"
        }
    }


@app.post("/api/3d-videos", response_model=JobResponse)
async def create_3d_video(request: Video3DRequest, background_tasks: BackgroundTasks):
    """
    Create a new 3D video generation job
    
    The job is processed asynchronously in the background.
    Use the returned job_id to check status and download the video.
    """
    # Create job
    job_id = job_manager.create_job(
        prompt=request.prompt,
        quality=request.quality,
        category=request.category,
        scene_name=request.scene_name
    )
    
    logger.info(f"📝 New 3D job created: {job_id} (quality: {request.quality}, category: {request.category})")
    
    # Start generation in background
    background_tasks.add_task(video_generator.generate_video, job_id)
    
    return JobResponse(
        job_id=job_id,
        status=JobStatus.PENDING,
        category=request.category,
        message="3D video job created successfully. Generation started.",
        created_at=datetime.now().isoformat()
    )


@app.get("/api/3d-jobs/{job_id}", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    """
    Get the status of a 3D video generation job
    
    Returns current status, progress, and video URL if completed.
    """
    job = job_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    video_url = None
    duration = None
    
    if job["status"] == JobStatus.COMPLETED and job.get("video_path"):
        video_url = f"/api/3d-videos/{job_id}"
        
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
        category=job["category"],
        progress=job["progress"],
        created_at=job["created_at"],
        updated_at=job["updated_at"],
        error=job.get("error"),
        video_url=video_url,
        duration=duration
    )


@app.get("/api/3d-videos/{job_id}")
async def download_video(job_id: str):
    """
    Download the generated 3D video file
    
    Returns the MP4 file if the job is completed successfully.
    """
    job = job_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job["status"] != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"3D video not ready. Current status: {job['status']}"
        )
    
    video_path = Path(job["video_path"])
    
    if not video_path.exists():
        raise HTTPException(status_code=404, detail="3D video file not found")
    
    return FileResponse(
        video_path,
        media_type="video/mp4",
        filename=f"{job['scene_name']}_3D.mp4"
    )


@app.get("/api/3d-jobs")
async def list_jobs(limit: int = 50):
    """
    List all 3D video generation jobs
    
    Returns a list of jobs sorted by creation time (most recent first).
    """
    jobs = job_manager.list_jobs(limit=limit)
    
    return {
        "total": len(jobs),
        "jobs": jobs
    }


@app.delete("/api/3d-jobs/{job_id}")
async def delete_job(job_id: str):
    """Delete a 3D job and its associated files"""
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
    
    return {"message": "3D job deleted successfully", "job_id": job_id}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "3D Video Generation",
        "timestamp": datetime.now().isoformat(),
        "jobs": {
            "total": len(job_manager.jobs),
            "pending": len([j for j in job_manager.jobs.values() if j["status"] == JobStatus.PENDING]),
            "processing": len([j for j in job_manager.jobs.values() if j["status"] in [JobStatus.GENERATING_CODE, JobStatus.RENDERING]]),
            "completed": len([j for j in job_manager.jobs.values() if j["status"] == JobStatus.COMPLETED]),
            "failed": len([j for j in job_manager.jobs.values() if j["status"] == JobStatus.FAILED])
        },
        "categories": {
            "mathematical": len([j for j in job_manager.jobs.values() if j.get("category") == "mathematical"]),
            "scientific": len([j for j in job_manager.jobs.values() if j.get("category") == "scientific"]),
            "geometric": len([j for j in job_manager.jobs.values() if j.get("category") == "geometric"]),
            "data": len([j for j in job_manager.jobs.values() if j.get("category") == "data"]),
        }
    }


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting Manim 3D Video Generation API Server...")
    print("📚 API Documentation: http://localhost:8001/docs")
    print("🔍 ReDoc Documentation: http://localhost:8001/redoc")
    print("🎯 STEM Categories: Mathematical, Scientific, Geometric, Data Visualization")
    
    uvicorn.run(
        "api_server_3d:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    )

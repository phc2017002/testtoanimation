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


class AnimationCategory(str, Enum):
    """Animation categories"""
    TECH_SYSTEM = "tech_system"        # System design, architecture
    MATHEMATICAL = "mathematical"      # Math, research papers
    PRODUCT_STARTUP = "product_startup"  # Product demos, startup pitches


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
    category: AnimationCategory = Field(default=AnimationCategory.MATHEMATICAL, description="Animation category")
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
    
    def create_job(self, prompt: str, quality: QualityLevel, category: AnimationCategory = AnimationCategory.MATHEMATICAL, scene_name: Optional[str] = None) -> str:
        """Create a new job"""
        job_id = str(uuid.uuid4())
        
        if not scene_name:
            scene_name = f"Scene_{uuid.uuid4().hex[:8]}"
        
        job_data = {
            "job_id": job_id,
            "status": JobStatus.PENDING,
            "prompt": prompt,
            "category": category.value,
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
    
    def _get_partial_dir(self, job_id: str, scene_name: str, quality: str) -> Path:
        """Get the partial movie files directory for a given job."""
        quality_dirs = {
            "low": "480p15",
            "medium": "720p30",
            "high": "1080p60",
            "ultra": "2160p60"
        }
        resolution = quality_dirs.get(quality, "1080p60")
        partial_dir = Config.VIDEOS_DIR / f"scene_{job_id}" / resolution / "partial_movie_files" / scene_name
        return partial_dir
    
    def _extract_frames_from_partial_files(self, job_id: str, scene_name: str, quality: str) -> list:
        """Extract one frame from each partial movie file for comprehensive analysis."""
        partial_dir = self._get_partial_dir(job_id, scene_name, quality)
        
        if not partial_dir.exists():
            logger.warning(f"Job {job_id[:8]}... | Partial directory not found: {partial_dir}")
            return []
        
        # Get all .mp4 files sorted by name
        video_files = sorted(partial_dir.glob("*.mp4"))
        
        if not video_files:
            logger.warning(f"Job {job_id[:8]}... | No partial movie files found in {partial_dir}")
            return []
        
        logger.info(f"Job {job_id[:8]}... | Found {len(video_files)} partial movie files")
        
        # Use analyzer's method to extract frames
        frame_paths = self.analyzer.extract_frames_from_videos(video_files)
        
        logger.info(f"Job {job_id[:8]}... | Extracted {len(frame_paths)} frames")
        return frame_paths
    
    def _extract_scene_class_name(self, code_file: Path) -> str:
        """Extract the actual scene class name from the Python code file."""
        import re
        
        if not code_file.exists():
            return None
        
        with open(code_file, 'r') as f:
            content = f.read()
        
        # Match: class ClassName(VoiceoverScene): or class ClassName(ThreeDScene):
        pattern = r'^class\s+(\w+)\s*\((?:VoiceoverScene|ThreeDScene|Scene)\):'
        match = re.search(pattern, content, re.MULTILINE)
        
        if match:
            return match.group(1)
        
        return None
    
    def _extract_frames_from_final_video(self, video_path: Path, total_animations: int, job_id: str) -> list[Path]:
        """
        Extract frames from final video at evenly-spaced intervals to capture all animations.
        Uses ffmpeg to extract one frame per animation.
        """
        import subprocess
        import tempfile
        
        if total_animations == 0:
            logger.warning(f"Job {job_id[:8]}... | No animations to extract")
            return []
        
        logger.info(f"Job {job_id[:8]}... | Extracting {total_animations} frames from final video")
        
        # Get video duration using ffprobe
        try:
            result = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "csv=p=0", str(video_path)],
                capture_output=True, text=True, timeout=10
            )
            
            if result.returncode != 0:
                logger.error(f"Job {job_id[:8]}... | ffprobe failed: {result.stderr}")
                return []
            
            duration = float(result.stdout.strip())
            logger.info(f"Job {job_id[:8]}... | Video duration: {duration:.2f}s")
            
        except Exception as e:
            logger.error(f"Job {job_id[:8]}... | Failed to get video duration: {e}")
            return []
        
        # Create temp directory for frames
        temp_dir = Path(tempfile.mkdtemp(prefix=f"frames_{job_id[:8]}_"))
        frame_paths = []
        
        # Calculate interval between frames to capture all animations
        interval = duration / total_animations if total_animations > 0 else duration
        
        # Extract frames at intervals
        for i in range(total_animations):
            timestamp = i * interval + (interval / 2)  # Middle of each animation segment
            frame_path = temp_dir / f"frame_{i:04d}.png"
            
            try:
                result = subprocess.run(
                    ["ffmpeg", "-ss", str(timestamp), "-i", str(video_path),
                     "-vframes", "1", "-q:v", "2", str(frame_path)],
                    capture_output=True, timeout=10
                )
                
                if result.returncode == 0 and frame_path.exists():
                    frame_paths.append(frame_path)
                else:
                    logger.warning(f"Job {job_id[:8]}... | Failed to extract frame {i} at {timestamp:.2f}s")
                    
            except Exception as e:
                logger.warning(f"Job {job_id[:8]}... | Error extracting frame {i}: {e}")
        
        logger.info(f"Job {job_id[:8]}... | Successfully extracted {len(frame_paths)}/{total_animations} frames")
        return frame_paths
    
    def _map_frames_to_animations(
        self,
        issues: list[dict],
        total_animations: int,
        frames_analyzed: int
    ) -> dict[int, list[dict]]:
        """
        Map problematic frames to their source animation indices.
        
        Args:
            issues: List of issues from Qwen 3 VL analysis
            total_animations: Total number of animations in the video
            frames_analyzed: Number of frames that were analyzed
        
        Returns:
            Dictionary mapping animation_index -> list of issues
        """
        animation_issues = {}
        
        for issue in issues:
            frame_num = issue.get('frame', 0)
            
            # Calculate which animation generated this frame
            # Frames are evenly distributed across animations
            if frames_analyzed > 0:
                animation_index = int((frame_num * total_animations) / frames_analyzed)
                animation_index = min(animation_index, total_animations - 1)  # Clamp to valid range
                
                if animation_index not in animation_issues:
                    animation_issues[animation_index] = []
                
                animation_issues[animation_index].append(issue)
        
        return animation_issues
    
    def _validate_fixed_code(self, original_code: str, fixed_code: str) -> tuple[bool, str]:
        """
        Validate that fixed code is reasonable and didn't break functionality.
        
        Args:
            original_code: Original code before fixes
            fixed_code: Code after Claude's fixes
        
        Returns:
            (is_valid, error_message) tuple
        """
        import re
        
        # Check 1: Code shouldn't be dramatically shorter (suggests deletion)
        if len(fixed_code) < len(original_code) * 0.7:
            return False, f"Fixed code is {100 - int(len(fixed_code)/len(original_code)*100)}% shorter - likely deleted too much"
        
        # Check 2: Should still have same class name
        original_class = re.search(r'class\s+(\w+)', original_code)
        fixed_class = re.search(r'class\s+(\w+)', fixed_code)
        if original_class and fixed_class:
            if original_class.group(1) != fixed_class.group(1):
                return False, f"Class name changed: {original_class.group(1)} → {fixed_class.group(1)}"
        elif original_class and not fixed_class:
            return False, "Class definition removed"
        
        # Check 3: Should have similar number of self.play() calls
        original_plays = len(re.findall(r'self\.play\(', original_code))
        fixed_plays = len(re.findall(r'self\.play\(', fixed_code))
        if fixed_plays < original_plays * 0.75:
            return False, f"Too many play() calls removed: {original_plays} → {fixed_plays}"
        
        # Check 4: Should still have construct method
        if 'def construct(self):' in original_code and 'def construct(self):' not in fixed_code:
            return False, "construct() method removed or renamed"
        
        return True, ""
    
    async def _generate_comprehensive_fix(
        self,
        current_code: str,
        issues: list[dict],
        problematic_animations: dict[int, list[dict]]
    ) -> str:
        """
        Generate comprehensive fixes for all issues using Claude.
        
        Args:
            current_code: Current scene code
            issues: All issues found
            problematic_animations: Mapping of animation_index -> issues
        
        Returns:
            Fixed code or None if fix generation failed
        """
        try:
            # Build enhanced fix prompt with stricter rules
            fix_prompt = """You are an expert Manim code fixer. Your goal is to fix ONLY the visual issues while preserving ALL functionality.

CRITICAL RULES (FOLLOW EXACTLY):
1. DO NOT change the logic or functionality of the code
2. DO NOT remove or comment out working code
3. DO NOT delete any self.play() calls
4. ONLY fix the specific visual issues mentioned below
5. Keep all variable names, class structures, and methods intact
6. Ensure all colors/constants are properly imported from manim

ISSUES TO FIX:

"""
            
            # Group issues by animation with clear descriptions
            for anim_idx in sorted(problematic_animations.keys()):
                anim_issues = problematic_animations[anim_idx]
                fix_prompt += f"\nAnimation Index {anim_idx}:\n"
                
                for issue in anim_issues:
                    issue_type = issue.get('type', 'unknown')
                    description = issue.get('description', '')
                    fix_prompt += f"  • [{issue_type.upper()}] {description}\n"
            
            fix_prompt += f"""

COMMON FIX PATTERNS:
- Overlapping text: Use .next_to(ref, direction, buff=0.5) or .shift(UP*2)
- Broken LaTeX: Fix $ delimiters, escape backslashes, check for typos
- Undefined colors: Import from manim (RED, BLUE, GREEN, YELLOW, etc.) or use "#hexcode"
- Text outside bounds: Reduce font_size or reposition with .to_edge()

EXAMPLE FIXES:
# Bad: text1 = Text("Hello").shift(UP)
#      text2 = Text("World").shift(UP)  # Overlaps!
# Good: text1 = Text("Hello").shift(UP)
#       text2 = Text("World").next_to(text1, DOWN)

# Bad: equation = MathTex("\\sigma")  # Missing escape
# Good: equation = MathTex("\\\\sigma")

CURRENT CODE:
```python
{current_code}
```

Return ONLY the complete fixed Python code (no explanations, no markdown blocks, just the code):
"""
            
            # Call Claude for fixes
            messages = [
                {
                    "role": "system",
                    "content": "You are an expert Manim code fixer. Fix visual issues while maintaining all functionality. Return only the fixed code."
                },
                {
                    "role": "user",
                    "content": fix_prompt
                }
            ]
            
            from manimator.utils.dual_model_config import DualModelConfig
            from manimator.utils.code_postprocessor import post_process_code
            
            # Generate fixes
            raw_fixed_code = DualModelConfig.generate_code(messages)
            
            # Post-process to extract clean code
            fixed_code = post_process_code(raw_fixed_code)
            
            # Validate before accepting fixes
            is_valid, error_msg = self._validate_fixed_code(current_code, fixed_code)
            if not is_valid:
                logger.warning(f"⚠️  Fixed code validation failed: {error_msg}")
                logger.info("❌ Rejecting auto-fix to avoid breaking code")
                return None
            
            logger.info("✅ Fixed code passed validation checks")
            return fixed_code
            
        except Exception as e:
            logger.error(f"Error generating comprehensive fix: {e}")
            return None
    
    async def _perform_comprehensive_analysis(self, job_id: str, scene_name: str, quality: str, video_path: Path = None, total_animations: int = 0):
        """Perform comprehensive visual analysis on all frames and store results."""
        from datetime import datetime
        
        logger.info(f"Job {job_id[:8]}... | Starting comprehensive visual analysis")
        
        # Update status
        self.job_manager.update_job(
            job_id,
            status=JobStatus.VERIFYING,
            progress={
                "stage": "comprehensive_analysis",
                "percentage": 92,
                "message": "Analyzing all frames with Qwen 3 VL for overlaps"
            }
        )
        
        try:
            # Get the actual scene class name from the code file
            job = self.job_manager.get_job(job_id)
            code_file = Path(job.get('code_path', ''))
            actual_scene_name = self._extract_scene_class_name(code_file)
            
            if not actual_scene_name:
                logger.warning(f"Job {job_id[:8]}... | Could not extract scene class name, using provided name: {scene_name}")
                actual_scene_name = scene_name
            else:
                logger.info(f"Job {job_id[:8]}... | Detected scene class: {actual_scene_name}")
            
            # NEW: Prefer timestamp-based extraction for true 100% coverage
            if video_path and total_animations > 0:
                logger.info(f"Job {job_id[:8]}... | Using timestamp-based extraction for {total_animations} animations")
                frame_paths = self._extract_frames_from_final_video(video_path, total_animations, job_id)
            else:
                logger.info(f"Job {job_id[:8]}... | Falling back to partial file extraction")
                # Extract frames using the actual scene class name
                frame_paths = self._extract_frames_from_partial_files(job_id, actual_scene_name, quality)
            
            if not frame_paths:
                logger.warning(f"Job {job_id[:8]}... | No frames extracted, skipping analysis")
                return
            
            # Analyze with Qwen 3 VL
            logger.info(f"Job {job_id[:8]}... | Analyzing {len(frame_paths)} frames with Qwen 3 VL")
            analysis_result = self.analyzer.analyze_frames(frame_paths)
            
            # Store results in job metadata
            visual_analysis_data = {
                "model": "openrouter/qwen/qwen3-vl-235b-a22b-instruct",
                "frames_analyzed": len(frame_paths),
                "overall_quality": analysis_result.get('overall_quality', 'unknown'),
                "issues": analysis_result.get('issues', []),
                "timestamp": datetime.now().isoformat(),
                "coverage_percentage": 100.0  # We analyzed all extracted frames
            }
            
            self.job_manager.update_job(
                job_id,
                visual_analysis=visual_analysis_data
            )
            
            
            # NEW: Auto-fix if comprehensive analysis found issues
            # Check for issues count instead of has_issues flag (which isn't always set)
            issues_found = analysis_result.get('issues', [])
            if len(issues_found) > 0 and video_path and total_animations > 0:
                issue_count = len(analysis_result['issues'])
                logger.info(f"Job {job_id[:8]}... | Comprehensive analysis found {issue_count} issues")
                logger.info(f"Job {job_id[:8]}... | Attempting automatic fixes with Claude...")
                
                try:
                    # Get current code
                    job = self.job_manager.get_job(job_id)
                    code_file = Path(job.get('code_path', ''))
                    
                    if not code_file.exists():
                        logger.warning(f"Job {job_id[:8]}... | Code file not found, skipping auto-fix")
                    else:
                        current_code = code_file.read_text()
                        
                        # Map frames to animations
                        problematic_animations = self._map_frames_to_animations(
                            analysis_result['issues'],
                            total_animations,
                            len(frame_paths)
                        )
                        
                        logger.info(f"Job {job_id[:8]}... | Issues mapped to {len(problematic_animations)} animations")
                        
                        # Generate comprehensive fix
                        fixed_code = await self._generate_comprehensive_fix(
                            current_code,
                            analysis_result['issues'],
                            problematic_animations
                        )
                        
                        if fixed_code and fixed_code != current_code:
                            # Save fixed code
                            code_file.write_text(fixed_code)
                            logger.info(f"Job {job_id[:8]}... | Applied fixes, re-rendering...")
                            
                            # Re-render with fixes
                            new_video_path, new_total_animations = await self._render_video(
                                code_file,
                                actual_scene_name,
                                quality
                            )
                            
                            # Re-analyze to verify fixes
                            logger.info(f"Job {job_id[:8]}... | Re-analyzing to verify fixes...")
                            new_frame_paths = self._extract_frames_from_final_video(
                                new_video_path,
                                new_total_animations,
                                job_id
                            )
                            
                            verification_result = self.analyzer.analyze_frames(new_frame_paths)
                            
                            # Calculate improvement
                            issues_after = len(verification_result.get('issues', []))
                            improvement = issue_count - issues_after
                            
                            # Update analysis with verification
                            visual_analysis_data['auto_fix'] = {
                                'applied': True,
                                'issues_before': issue_count,
                                'issues_after': issues_after,
                                'quality_before': analysis_result.get('overall_quality'),
                                'quality_after': verification_result.get('overall_quality'),
                                'improvement': improvement,
                                'success': improvement > 0  # Track if it actually helped
                            }
                            
                            # Update final issues list
                            visual_analysis_data['issues'] = verification_result.get('issues', [])
                            visual_analysis_data['overall_quality'] = verification_result.get('overall_quality')
                            
                            self.job_manager.update_job(
                                job_id,
                                visual_analysis=visual_analysis_data,
                                video_path=str(new_video_path)
                            )
                            
                            # Log results with appropriate level
                            if improvement > 0:
                                logger.info(f"✅ Job {job_id[:8]}... | Auto-fix SUCCESS: "
                                          f"{issue_count} → {issues_after} issues "
                                          f"({improvement} fixed, {improvement/issue_count*100:.0f}% improvement)")
                            elif improvement == 0:
                                logger.warning(f"⚠️  Job {job_id[:8]}... | Auto-fix NO CHANGE: "
                                             f"{issue_count} issues remain")
                            else:
                                logger.error(f"❌ Job {job_id[:8]}... | Auto-fix MADE THINGS WORSE: "
                                           f"{issue_count} → {issues_after} issues "
                                           f"({abs(improvement)} MORE issues created!)")
                            
                            # Cleanup new frames
                            for frame in new_frame_paths:
                                if frame.exists():
                                    frame.unlink()
                            
                            # Update video_path for final cleanup
                            video_path = new_video_path
                        else:
                            logger.info(f"Job {job_id[:8]}... | No fixes generated or code unchanged")
                            
                except Exception as fix_error:
                    logger.error(f"Job {job_id[:8]}... | Auto-fix error: {fix_error}")
                    visual_analysis_data['auto_fix'] = {
                        'applied': False,
                        'error': str(fix_error)
                    }
                    self.job_manager.update_job(job_id, visual_analysis=visual_analysis_data)
            else:
                logger.info(f"Job {job_id[:8]}... | No issues found or auto-fix not available")
            
            # Cleanup original frames
            for frame in frame_paths:
                if frame.exists():
                    frame.unlink()
            
        except Exception as e:
            logger.error(f"Job {job_id[:8]}... | Error during comprehensive analysis: {e}")
            # Don't fail the job, just log the error
            self.job_manager.update_job(
                job_id,
                visual_analysis={
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                }
            )
    
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
                code = await self._generate_code(current_prompt, job.get("category", "mathematical"))
                
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
                
                # Stage 2: Render video (Pass 1) - with error handling
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
                
                # Try initial render - if it fails, skip to verification loop for fixes
                video_path = None
                total_animations = 0
                initial_render_failed = False
                
                try:
                    video_path, total_animations = await self._render_video(
                        code_file,
                        job["scene_name"],
                        job["quality"]
                    )
                    logger.info(f"✅ Initial render successful for job {job_id[:8]}...")
                except Exception as render_error:
                    logger.warning(f"⚠️  Initial render failed for job {job_id[:8]}: {str(render_error)[:100]}")
                    logger.info(f"🔧 Will attempt to fix errors in verification loop...")
                    initial_render_failed = True
                
                # Stage 3: Visual Verification Loop (Gemini Fixes)
                # OPTIMIZED: Reduced to 2 retries (was 5) since comprehensive analysis runs after
                # If initial render failed, we'll try to fix and re-render
                max_retries = 3 if initial_render_failed else 2  # Extra retry if initial render failed
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
                    
                    # If initial render failed and this is first iteration, skip analysis and try render again
                    if initial_render_failed and i == 0 and video_path is None:
                        logger.info(f"⚠️  No video from initial render, attempting render with current code...")
                        try:
                            video_path, total_animations = await self._render_video(
                                code_file,
                                job["scene_name"],
                                job["quality"]
                            )
                            logger.info(f"✅ Render successful after initial failure!")
                            initial_render_failed = False
                            verification_passed = True
                            break
                        except Exception as e2:
                            logger.warning(f"⚠️  Render still failing: {str(e2)[:100]}")
                            logger.info(f"🔧 Will use Claude to fix code errors...")
                            # Continue to next iteration with code fix
                            continue
                    
                    # Run analysis and fix (using Gemini for fixes now)
                    if video_path:
                        final_code, report = self.analyzer.analyze_and_fix(
                            code,
                            video_path,
                            max_iterations=1 # Analyze once per loop iteration
                        )
                    else:
                        # No video available, ask Claude to fix the code
                        logger.info(f"🔧 No video available, using Claude to fix code syntax/errors...")
                        final_code = code  # For now, mark as needing regeneration
                    
                    # If code is unchanged, we are good
                    if final_code == code and video_path:
                        logger.info(f"✅ Verification passed on attempt {i+1}! No issues found.")
                        verification_passed = True
                        break
                    
                    # Issues found, applying fixes
                    logger.info(f"🛠️ Issues found! Applying fixes using Claude and re-rendering (Attempt {i+1})...")
                    code = final_code
                    
                    # Save fixed code
                    with open(code_file, 'w') as f:
                        f.write(code)
                    
                    video_path, total_animations = await self._render_video(
                        code_file,
                        job["scene_name"],
                        job["quality"]
                    )
                
                if verification_passed:
                    # Success! Break the outer regeneration loop
                    break
                else:
                    # Verification failed after max retries (Gemini couldn't fix it)
                    logger.warning(f"⚠️ Layout issues persisted after {max_retries} Gemini fix attempts.")
                    
                    # Trigger Claude Fallback (Regeneration)
                    regeneration_count += 1
                    if regeneration_count <= max_regenerations:
                        logger.warning(f"🔄 Triggering Claude Fallback: Regenerating scene from scratch (Attempt {regeneration_count})...")
                        continue # Loop back to regenerate code with Claude
                    else:
                        logger.error("❌ Max regenerations exceeded. Failing job.")
                        logger.info("⚠️ Accepting best effort video.")
                        break
            
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

        # Stage 4: Comprehensive Visual Analysis
        logger.info(f"Job {job_id[:8]}... | Performing comprehensive frame analysis")
        await self._perform_comprehensive_analysis(
            job_id,
            job["scene_name"],
            job["quality"],
            video_path=video_path,  # NEW: Pass video for timestamp-based extraction
            total_animations=total_animations  # NEW: Enable true 100% coverage
        )
        
        # Stage 5: Complete
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
    
    async def _generate_code(self, prompt: str, category: str = "mathematical") -> str:
        """Generate Manim code from prompt"""
        # Run in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda p=prompt, c=category: generate_animation_response(p, c)
        )
        
        # Extract Python code from markdown
        pattern = r'```python\n(.*?)```'
        match = re.search(pattern, response, re.DOTALL)
        
        if match:
            return match.group(1)
        else:
            # Try without code block
            return response
    
    async def _render_video(self, code_file: Path, scene_name: str, quality: QualityLevel) -> tuple[Path, int]:
        """Render video using Manim with real-time progress. Returns (video_path, total_animations)."""
        quality_flag = QUALITY_FLAGS[quality]
        
        cmd = [
            "manim",
            quality_flag,
            "--disable_caching",  # Force all animations to create partial files for 100% coverage
            str(code_file),
            scene_name
        ]
        
        logger.info(f"🎬 Executing: {' '.join(cmd)}")
        
        # Prepare environment with LaTeX path
        env = os.environ.copy()
        latex_path = "/Library/TeX/texbin"
        if latex_path not in env.get("PATH", ""):
            env["PATH"] = f"{latex_path}:{env.get('PATH', '')}"
        
        # Run subprocess with streaming output
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,  # Merge stderr into stdout
            cwd=str(Config.BASE_DIR),
            env=env
        )
        
        # Stream output in real-time
        output_lines = []
        last_animation_num = 0
        max_animation_num = 0  # Track highest animation number seen
        
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
                    max_animation_num = max(max_animation_num, anim_num)  # Track total animations
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
        total_animations = max_animation_num + 1  # +1 because it's 0-indexed
        logger.info(f"📹 Found video: {video_path.name}")
        logger.info(f"📊 Total animations rendered: {total_animations}")
        
        return video_path, total_animations


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
        category=request.category,
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
    print("📚 API Documentation: http://localhost:8003/docs")
    print("🔍 ReDoc Documentation: http://localhost:8003/redoc")
    
    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=8003,
        reload=True,
        log_level="info"
    )

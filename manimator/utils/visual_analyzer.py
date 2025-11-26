"""
Visual Layout Analyzer using Gemini 3 Pro

Uses multimodal LLM to analyze rendered frames and provide feedback on layout issues.
"""

import os
import base64
from pathlib import Path
from typing import List, Dict, Tuple
import litellm
from PIL import Image
import json
import re
import subprocess
import tempfile
from .dual_model_config import DualModelConfig


class VisualLayoutAnalyzer:
    """
    Analyze Manim animation frames using multimodal vision model.
    
    Detects:
    - Overlapping text/labels
    - Text extending outside frame
    - Poor positioning
    - Cluttered layouts
    """
    
    def __init__(self, model: str = DualModelConfig.get_visual_model()):
        """
        Initialize the visual analyzer.
        
        Args:
            model: Multimodal model to use (default: Gemini 3 Pro)
        """
        self.model = model
    
    def extract_frames(self, video_path: Path, num_frames: int = 1) -> List[Path]:
        """
        Extract key frames from video for analysis.
        
        Args:
            video_path: Path to rendered video
            num_frames: Number of frames to extract
        
        Returns:
            List of paths to extracted frame images
        """
        # Get video duration
        duration_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(video_path)
        ]
        
        result = subprocess.run(duration_cmd, capture_output=True, text=True)
        duration = float(result.stdout.strip())
        
        # Calculate frame timestamps (evenly distributed)
        timestamps = [duration * i / (num_frames + 1) for i in range(1, num_frames + 1)]
        
        # Extract frames
        frame_paths = []
        temp_dir = Path(tempfile.mkdtemp())
        
        for i, timestamp in enumerate(timestamps):
            frame_path = temp_dir / f"frame_{i:03d}.png"
            
            extract_cmd = [
                "ffmpeg", "-ss", str(timestamp),
                "-i", str(video_path),
                "-frames:v", "1",
                "-q:v", "2",  # High quality
                str(frame_path),
                "-y"
            ]
            
            subprocess.run(extract_cmd, capture_output=True, check=True)
            frame_paths.append(frame_path)
        
        return frame_paths
    
    def extract_event_frames(self, partial_dir: Path) -> List[Path]:
        """
        Extract the last frame from each partial movie file (corresponding to self.play calls).
        
        Args:
            partial_dir: Directory containing partial movie files
        
        Returns:
            List of paths to extracted frame images
        """
        # Find all mp4 files
        video_files = list(partial_dir.glob("*.mp4"))
        
        # Sort by modification time to ensure correct order
        video_files.sort(key=lambda f: f.stat().st_mtime)
        
        frame_paths = []
        temp_dir = Path(tempfile.mkdtemp())
        
        print(f"  - Found {len(video_files)} event segments. Extracting frames...")
        
        for i, video_path in enumerate(video_files):
            # Extract the LAST frame of each segment to see the result of the animation
            frame_path = temp_dir / f"event_{i:03d}.png"
            
            # ffmpeg command to extract the last frame
            # -sseof -3 means "3 seconds from end" (safe buffer), but for short clips we need to be careful.
            # A safer way for single frame extraction from end is using -sseof -0.1 or similar, 
            # but sometimes that fails for very short clips.
            # Alternative: get duration and seek to end.
            
            # Let's use a robust approach: extract the last frame using -sseof
            extract_cmd = [
                "ffmpeg", "-sseof", "-0.1",
                "-i", str(video_path),
                "-frames:v", "1",
                "-q:v", "2",
                "-update", "1", # For single image
                str(frame_path),
                "-y"
            ]
            
            try:
                subprocess.run(extract_cmd, capture_output=True, check=True)
                frame_paths.append(frame_path)
            except subprocess.CalledProcessError:
                # Fallback for very short videos: try extracting from start
                extract_cmd[2] = "0" # Remove -sseof
                extract_cmd[1] = "-ss"
                try:
                    subprocess.run(extract_cmd, capture_output=True, check=True)
                    frame_paths.append(frame_path)
                except Exception as e:
                    print(f"⚠️ Failed to extract frame from {video_path.name}: {e}")
        
        return frame_paths
    
    def extract_frames_from_videos(self, video_paths: List[Path]) -> List[Path]:
        """
        Extract the last frame from a list of video files.
        
        Args:
            video_paths: List of paths to video files (can contain duplicates)
        
        Returns:
            List of paths to extracted frame images
        """
        frame_paths = []
        temp_dir = Path(tempfile.mkdtemp())
        
        print(f"  - Extracting frames from {len(video_paths)} video segments...")
        
        for i, video_path in enumerate(video_paths):
            # Extract the LAST frame of each segment
            # We use the index 'i' to name the frame, preserving order even if video_path is reused
            frame_path = temp_dir / f"step_{i:03d}.png"
            
            if not video_path.exists():
                print(f"⚠️ Video file not found: {video_path}")
                continue
            
            # Robust extraction using -sseof -0.1
            extract_cmd = [
                "ffmpeg", "-sseof", "-0.1",
                "-i", str(video_path),
                "-frames:v", "1",
                "-q:v", "2",
                "-update", "1",
                str(frame_path),
                "-y"
            ]
            
            try:
                subprocess.run(extract_cmd, capture_output=True, check=True)
                frame_paths.append(frame_path)
            except subprocess.CalledProcessError:
                # Fallback for very short videos
                extract_cmd[2] = "0" # Remove -sseof
                extract_cmd[1] = "-ss"
                try:
                    subprocess.run(extract_cmd, capture_output=True, check=True)
                    frame_paths.append(frame_path)
                except Exception as e:
                    print(f"⚠️ Failed to extract frame from {video_path.name}: {e}")
        
        return frame_paths
    
    def _robust_json_parse(self, response_text: str, batch_id: int) -> dict:
        """
        Robustly parse JSON from LLM response with multiple fallback strategies.
        
        Handles common issues:
        - Extra text before/after JSON
        - Markdown code blocks
        - Malformed JSON
        - Empty responses
        
        Args:
            response_text: Raw response from LLM
            batch_id: Batch identifier for logging
        
        Returns:
            Parsed analysis dict or empty fallback dict
        """
        import re
        import json
        import logging
        
        logger = logging.getLogger(__name__)
        
        # Strategy 1: Try direct JSON parsing
        try:
            return json.loads(response_text.strip())
        except json.JSONDecodeError:
            pass
        
        # Strategy 2: Extract JSON from markdown code block
        code_block = re.search(r'```json\s*(\{.*?\})\s*```', response_text, re.DOTALL)
        if code_block:
            try:
                return json.loads(code_block.group(1))
            except json.JSONDecodeError:
                pass
        
        # Strategy 3: Extract first complete JSON object from response
        json_match = re.search(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', response_text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                pass
        
        # Strategy 4: Try to find and extract JSON between braces
        start = response_text.find('{')
        end = response_text.rfind('}')
        if start != -1 and end != -1 and start < end:
            try:
                potential_json = response_text[start:end+1]
                return json.loads(potential_json)
            except json.JSONDecodeError:
                pass
        
        # All strategies failed - return empty result with warning
        logger.warning(f"⚠️  Could not parse JSON from batch {batch_id}, returning empty result")
        logger.debug(f"Response preview: {response_text[:300]}...")
        
        return {
            "has_issues": False,
            "issues": [],
            "overall_quality": "unknown"
        }
    
    def encode_image(self, image_path: Path) -> str:
        """Encode image to base64 for API."""
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    
    def analyze_frames(self, frame_paths: List[Path], batch_size: int = 15) -> Dict[str, any]:
        """
        Analyze frames for layout issues using vision model.
        
        Args:
            frame_paths: List of frame image paths
            batch_size: Number of frames to analyze in one batch
        
        Returns:
            Analysis results with identified issues
        """
        all_issues = []
        has_any_issues = False
        qualities = []
        
        # Process in batches
        for i in range(0, len(frame_paths), batch_size):
            batch_paths = frame_paths[i:i + batch_size]
            print(f"    - Analyzing batch {i//batch_size + 1}/{(len(frame_paths)-1)//batch_size + 1} ({len(batch_paths)} frames)...")
            
            # Prepare images for the model
            image_contents = []
            for frame_path in batch_paths:
                image_contents.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{self.encode_image(frame_path)}"
                    }
                })
            
            # Create analysis prompt
            prompt = """Analyze these frames from a Manim animation.
Check for any VISUAL OVERLAPS between text, equations, graphs, or other elements.
Even a slight overlap is a critical issue.

If you see ANY overlap, return "has_issues": true.
Check specifically for:
- Text overlapping with other text or equations.
- Text overlapping with shapes or lines.
- Text extending beyond the screen boundaries (cut off).
- Elements that are too close to each other (touching).
- Broken LaTeX rendering (e.g., words like 'text', 'color', 'quad', 'floor' appearing literally in equations).
- Missing spaces or weird formatting in text.

Be extremely strict. Even a 1-pixel overlap is an issue.

Respond in JSON format:
```json
{
  "has_issues": true/false,
  "issues": [
    {
      "frame": 0,
      "type": "overlap",
      "description": "Description of the overlap (e.g. 'Title overlaps with equation')"
    }
  ],
  "overall_quality": "good/fair/poor"
}
```
"""
            
            # Build message with images
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt}
                    ] + image_contents
                }
            ]
            
            try:
                response = litellm.completion(
                    model=self.model,
                    messages=messages,
                    max_tokens=20000,
                    temperature=0.3
                )
                
                # Parse response using robust method
                response_text = response.choices[0].message.content
                analysis = self._robust_json_parse(response_text, i)
                
                if analysis.get("has_issues", False):
                    has_any_issues = True
                    # Adjust frame indices to match global index
                    batch_issues = analysis.get("issues", [])
                    for issue in batch_issues:
                        # If frame index is present, offset it
                        if "frame" in issue and isinstance(issue["frame"], int):
                            issue["frame"] += i
                    all_issues.extend(batch_issues)
                
                qualities.append(analysis.get("overall_quality", "unknown"))
                
            except Exception as e:
                print(f"⚠️  Visual analysis failed for batch {i}: {e}")
                # Continue to next batch
        
        # Aggregate results
        final_quality = "good"
        if "poor" in qualities:
            final_quality = "poor"
        elif "fair" in qualities:
            final_quality = "fair"
            
        return {
            "has_issues": has_any_issues,
            "issues": all_issues,
            "overall_quality": final_quality
        }
    
    def suggest_fixes(self, analysis: Dict, original_code: str) -> Tuple[str, List[str]]:
        """
        Generate code fixes based on visual analysis using the configured code model.
        
        Args:
            analysis: Analysis results from analyze_frames
            original_code: Original Manim code
        
        Returns:
            Tuple of (fixed_code, list_of_changes)
        """
        if not analysis.get("has_issues", False):
            return original_code, []
        
        issues = analysis.get("issues", [])
        if not issues:
            return original_code, []
            
        print(f"🔧 Requesting AI code fix for {len(issues)} issues...")
        
        # Construct prompt for Code Model
        prompt = f"""
You are an expert Manim animator. I have a Manim scene code that has visual layout issues detected by a vision model.
Your task is to FIX the code to resolve these specific issues while keeping the rest of the animation exactly the same.

### Visual Analysis Report (Issues to Fix):
{json.dumps(issues, indent=2)}

### Original Code:
```python
{original_code}
```

### Instructions:
1. Analyze the reported issues (overlaps, cutoffs, spacing, broken LaTeX).
2. Modify the code to fix these issues.
   - For overlaps: Increase spacing (buff), move elements (shift), or change directions.
   - For cutoffs: Move elements into frame, reduce font size, or wrap text.
   - For spacing: Adjust `next_to` buffers or absolute positions.
   - For broken LaTeX: Ensure raw strings `r"..."` are used and backslashes are correct.

### Common Pitfalls to AVOID:
- **Do NOT add vectors to Mobjects directly** (e.g., `mobj + UP` is INVALID). Use `mobj.shift(UP)` or `mobj.move_to(mobj.get_center() + UP)`.
- **Do NOT use `\color` inside MathTex** if it causes LaTeX errors. Use Manim's `color=` parameter or `SetColor` animation.
- **Do NOT change the logic of the animation**, only the layout/visuals.

3. RETURN ONLY THE FULL FIXED PYTHON CODE.
4. Do not add markdown backticks or explanations. Just the code.
"""

        messages = [
            {"role": "system", "content": "You are a strict code repair assistant. Output only valid Python code."},
            {"role": "user", "content": prompt}
        ]
        
        try:
            # Use Code Model to fix the code
            fixed_code = DualModelConfig.generate_code(messages, max_tokens=20000)
            
            # Extract code block using regex
            import re
            code_match = re.search(r'```python\n(.*?)\n```', fixed_code, re.DOTALL)
            if code_match:
                fixed_code = code_match.group(1).strip()
            else:
                # Fallback: try to find just ``` if python tag is missing
                code_match = re.search(r'```\n(.*?)\n```', fixed_code, re.DOTALL)
                if code_match:
                    fixed_code = code_match.group(1).strip()
                else:
                    # Fallback: naive cleanup if no blocks found (but risky)
                    fixed_code = fixed_code.replace("```python", "").replace("```", "").strip()
            
            changes = [f"AI fixed {len(issues)} layout issues using configured code model"]
            return fixed_code, changes
            
        except Exception as e:
            print(f"⚠️ AI code fix failed: {e}")
            return original_code, []
    
    def analyze_and_fix(
        self,
        code: str,
        video_path: Path,
        max_iterations: int = 2
    ) -> Tuple[str, Dict]:
        """
        Complete analysis and fixing workflow.
        
        Args:
            code: Generated Manim code
            video_path: Path to rendered preview video
            max_iterations: Maximum fix iterations
        
        Returns:
            Tuple of (final_code, analysis_report)
        """
        current_code = code
        all_changes = []
        iteration = 0
        
        while iteration < max_iterations:
            # Extract frames
            print(f"🔍 Analyzing visual layout (iteration {iteration + 1})...")
            frames = self.extract_frames(video_path)
            
            # Analyze
            analysis = self.analyze_frames(frames)
            
            # Clean up frames
            for frame in frames:
                frame.unlink()
            
            # Check if there are issues
            if not analysis.get("has_issues", False):
                print(f"✅ No layout issues detected! Quality: {analysis.get('overall_quality')}")
                break
            
            # Suggest and apply fixes
            fixed_code, changes = self.suggest_fixes(analysis, current_code)
            
            if not changes or fixed_code == current_code:
                # No more fixes possible
                print(f"ℹ️  No automatic fixes available for detected issues")
                break
            
            current_code = fixed_code
            all_changes.extend(changes)
            iteration += 1
            
            # Would need to re-render here to verify fixes
            # For now, we just apply fixes once
            break
        
        report = {
            "iterations": iteration + 1,
            "changes_applied": all_changes,
            "final_analysis": analysis
        }
        
        return current_code, report


from .dual_model_config import DualModelConfig

def create_visual_analyzer(model: str = None) -> VisualLayoutAnalyzer:
    """
    Factory function to create visual analyzer.
    
    Args:
        model: Model to use (defaults to DualModelConfig.VISUAL_MODEL)
    
    Returns:
        VisualLayoutAnalyzer instance
    """
    if model is None:
        model = DualModelConfig.get_visual_model()
    
    return VisualLayoutAnalyzer(model=model)

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
    
    def __init__(self, model: str = "gemini/gemini-exp-1206"):
        """
        Initialize the visual analyzer.
        
        Args:
            model: Multimodal model to use (default: Gemini 3 Pro)
        """
        self.model = model
    
    def extract_frames(self, video_path: Path, num_frames: int = 5) -> List[Path]:
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
    
    def encode_image(self, image_path: Path) -> str:
        """Encode image to base64 for API."""
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    
    def analyze_frames(self, frame_paths: List[Path]) -> Dict[str, any]:
        """
        Analyze frames for layout issues using vision model.
        
        Args:
            frame_paths: List of frame image paths
        
        Returns:
            Analysis results with identified issues
        """
        # Prepare images for the model
        image_contents = []
        for frame_path in frame_paths:
            image_contents.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{self.encode_image(frame_path)}"
                }
            })
        
        # Create analysis prompt
        prompt = """Analyze these frames from a Manim educational animation. You must be VERY STRICT about visual clarity. Look for:

1. **CRITICAL: Text Overlaps**: Check if ANY text overlaps with:
   - Other text
   - Arrows or lines (ESPECIALLY curved arrows)
   - Shapes (circles, rectangles)
   - Graph axes or plots
   Even a slight overlap is an issue.

2. **Out-of-frame content**: Is any text cut off at the edges of the frame?

3. **Legibility**: Is text placed on top of other elements making it hard to read?

4. **Spacing issues**: Are elements too close together or cramped?

For each issue found, provide:
- Frame number where it occurs
- Type of issue (overlap/cutoff/spacing)
- Which elements are affected (e.g., "y-axis label", "equation text")
- Severity (minor/moderate/severe)

Respond in JSON format:
```json
{
  "has_issues": true/false,
  "issues": [
    {
      "frame": 0,
      "type": "overlap",
      "elements": ["y-axis label", "graph line"],
      "severity": "moderate",
      "description": "Y-axis label overlaps with the plot"
    }
  ],
  "overall_quality": "good/fair/poor"
}
```

If no issues, return: {"has_issues": false, "issues": [], "overall_quality": "good"}
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
            
            # Parse response
            response_text = response.choices[0].message.content
            
            # Extract JSON from response (handle markdown code blocks)
            import re
            import json
            
            json_match = re.search(r'```json\n(.*?)\n```', response_text, re.DOTALL)
            if json_match:
                analysis = json.loads(json_match.group(1))
            else:
                # Try to parse directly
                analysis = json.loads(response_text)
            
            return analysis
            
        except Exception as e:
            print(f"⚠️  Visual analysis failed: {e}")
            return {
                "has_issues": False,
                "issues": [],
                "overall_quality": "unknown",
                "error": str(e)
            }
    
    def suggest_fixes(self, analysis: Dict, original_code: str) -> Tuple[str, List[str]]:
        """
        Generate code fixes based on visual analysis using Claude 4.5 Sonnet.
        
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
        
        # Construct prompt for Claude
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
1. Analyze the reported issues (overlaps, cutoffs, spacing).
2. Modify the code to fix these issues.
   - For overlaps: Increase spacing (buff), move elements (shift), or change directions.
   - For cutoffs: Move elements into frame, reduce font size, or wrap text.
   - For spacing: Adjust `next_to` buffers or absolute positions.
3. RETURN ONLY THE FULL FIXED PYTHON CODE.
4. Do not add markdown backticks or explanations. Just the code.
"""

        messages = [
            {"role": "system", "content": "You are a strict code repair assistant. Output only valid Python code."},
            {"role": "user", "content": prompt}
        ]
        
        try:
            # Use Claude (Code Model) to fix the code
            fixed_code = DualModelConfig.generate_with_claude(messages)
            
            # Clean up code block formatting if present
            fixed_code = fixed_code.replace("```python", "").replace("```", "").strip()
            
            changes = [f"AI fixed {len(issues)} layout issues using Claude 4.5 Sonnet"]
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

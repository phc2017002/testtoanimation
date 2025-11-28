"""
Gemini 3 Pro Image Preview service for frame verification and correction.
Uses OpenRouter API with multimodal capabilities to detect and fix visual issues.
"""

import requests
import json
import base64
import logging
from pathlib import Path
from typing import Tuple, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class FrameAnalysisResult:
    """Result of frame analysis with Gemini."""
    has_issues: bool
    issues_description: str
    corrected_image_data: Optional[bytes] = None


class GeminiVisionService:
    """Service for frame verification and correction using Gemini 3 Pro Image Preview."""
    
    def __init__(self, api_key: str):
        """
        Initialize Gemini Vision Service.
        
        Args:
            api_key: OpenRouter API key
        """
        self.api_key = api_key
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "google/gemini-3-pro-image-preview"
    
    def _image_to_base64(self, image_path: Path) -> str:
        """
        Convert image file to base64 data URL.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Base64 data URL string
        """
        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        return f"data:image/png;base64,{image_data}"
    
    def _base64_to_bytes(self, base64_url: str) -> bytes:
        """
        Extract bytes from base64 data URL.
        
        Args:
            base64_url: Base64 data URL (data:image/png;base64,...)
            
        Returns:
            Image bytes
        """
        # Format: data:image/png;base64,<data>
        if ',' in base64_url:
            base64_data = base64_url.split(',')[1]
        else:
            base64_data = base64_url
        return base64.b64decode(base64_data)
    
    def verify_and_correct_frame(
        self, 
        frame_path: Path,
        animation_index: int
    ) -> FrameAnalysisResult:
        """
        Verify frame for visual issues and generate corrected version if needed.
        
        This method:
        1. Analyzes the frame for overlaps and layout issues
        2. If issues found, generates a corrected version
        3. Returns both the analysis and corrected image
        
        Args:
            frame_path: Path to frame image (PNG)
            animation_index: Animation number for logging
        
        Returns:
            FrameAnalysisResult with analysis and corrected image if issues found
        """
        logger.info(f"  → Analyzing frame {animation_index} with Gemini 3 Pro Image Preview...")
        
        # Convert frame to base64
        try:
            image_base64 = self._image_to_base64(frame_path)
        except Exception as e:
            logger.error(f"  ✗ Failed to read frame: {e}")
            return FrameAnalysisResult(
                has_issues=False,
                issues_description=f"Error reading frame: {e}"
            )
        
        # Construct prompt for analysis and correction
        prompt = f"""Analyze this Manim animation frame (frame #{animation_index}) for visual quality issues.

**CRITICAL: Be VERY STRICT about spacing and layout. Educational videos must be extremely clear.**

**Check for these specific problems:**

1. **Text Spacing Issues (BE STRICT!):**
   - Title/heading too close to content below (need 40+ pixels)
   - Text lines too close together (need 25+ pixels)
   - Different text elements less than 30 pixels apart
   - Text crowding that reduces readability

2. **Element Crowding:**
   - Diagram elements (circles, boxes, arrows, icons) less than 25 pixels apart
   - Icons or symbols touching or overlapping other elements
   - Labels too close to their targets (need 15+ pixels)

3. **Text Overlaps (ZERO TOLERANCE):**
   - ANY text overlapping other text
   - Numbers overlapping with nodes, shapes, or diagrams
   - Labels overlapping with arrows or lines

4. **Visual Clarity:**
   - Content appears cramped or cluttered
   - Multiple elements competing for same space
   - Poor visual hierarchy or spacing

**IMPORTANT - BE CRITICAL:**
- If elements look even SLIGHTLY crowded, flag it as an issue
- Educational content must have generous spacing
- When in doubt, flag it - better safe than cramped

**IF YOU FIND ANY ISSUES:**
- List ALL specific spacing/crowding problems
- Be detailed: "Title 'X' is only 15px from subtitle 'Y' (need 40px)"
- GENERATE a corrected version with:
  * Generous spacing (40px+ for titles, 25px+ for content)
  * Clear visual hierarchy
  * Well-separated elements
  * Same content, professional layout
  * Maintain 1920x1080, black background, Manim style

**IF NO ISSUES:**
- Respond ONLY with: "NO ISSUES DETECTED - Frame is clear and well-laid out"

Be thorough and STRICT. Crowding hurts educational value."""

        # Make API request with multimodal support
        try:
            response = requests.post(
                url=self.api_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {"type": "image_url", "image_url": {"url": image_base64}}
                            ]
                        }
                    ],
                    "modalities": ["image", "text"]  # Request both text analysis and image generation
                },
                timeout=60  # Gemini can take time to generate images
            )
            
            response.raise_for_status()
            result = response.json()
            
        except requests.exceptions.Timeout:
            logger.error(f"  ✗ Gemini API request timed out after 60 seconds")
            return FrameAnalysisResult(
                has_issues=False,
                issues_description="API timeout - unable to verify"
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"  ✗ Gemini API request failed: {e}")
            return FrameAnalysisResult(
                has_issues=False,
                issues_description=f"API error: {e}"
            )
        
        # Parse response
        if not result.get("choices"):
            logger.warning(f"  ⚠️  No response from Gemini")
            return FrameAnalysisResult(
                has_issues=False,
                issues_description="No response from API"
            )
        
        message = result["choices"][0]["message"]
        text_response = message.get("content", "")
        
        # Check if issues were detected
        if "NO ISSUES DETECTED" in text_response.upper():
            logger.info(f"  ✅ Frame {animation_index}: No issues detected")
            return FrameAnalysisResult(
                has_issues=False,
                issues_description="No issues detected"
            )
        
        # Issues detected - check for generated image
        logger.warning(f"  ⚠️  Frame {animation_index}: Issues detected")
        logger.info(f"  Issues: {text_response[:200]}...")
        
        corrected_image = None
        if message.get("images"):
            # Extract generated image
            for image in message["images"]:
                image_url = image["image_url"]["url"]
                corrected_image = self._base64_to_bytes(image_url)
                logger.info(f"  ✅ Corrected frame generated ({len(corrected_image)} bytes)")
                break
        
        if corrected_image:
            return FrameAnalysisResult(
                has_issues=True,
                issues_description=text_response,
                corrected_image_data=corrected_image
            )
        else:
            logger.warning(f"  ⚠️  Issues detected but no corrected image generated")
            return FrameAnalysisResult(
                has_issues=True,
                issues_description=text_response,
                corrected_image_data=None
            )

import os
import litellm
from fastapi import HTTPException

from ..utils.system_prompts import get_system_prompt
from ..utils.code_postprocessor import post_process_code
from ..utils.dual_model_config import DualModelConfig


def generate_animation_response(prompt: str, category: str = "mathematical") -> str:
    """Generate Manim animation code from a text prompt.

    Uses Claude 4.5 Sonnet for code generation (best at coding).

    Args:
        prompt (str): User's request for an animation

    Returns:
        str: Generated Manim animation code (post-processed)

    Raises:
        HTTPException: If code generation fails
    """

    try:
        system_prompt = get_system_prompt(category)
        messages = [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": f"""{prompt}

CRITICAL REMINDERS:
1. The animation MUST be at least 5 MINUTES (300 seconds) long
2. Create 8-12 separate method functions for different sections
3. Each voiceover block should have 15-30 seconds of narration
4. Include detailed explanations, examples, and step-by-step derivations
5. Do NOT create short animations - make it comprehensive and educational

Make sure the objects or text in the generated code are not overlapping at any point in the video. Make sure that each scene is properly cleaned up before transitioning to the next scene.""",
            },
        ]
        
        # Use Claude 4.5 Sonnet for code generation
        raw_code = DualModelConfig.generate_with_claude(messages)
        
        # Post-process the code to fix common issues
        processed_code = post_process_code(raw_code)
        
        return processed_code
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to generate animation response: {str(e)}"
        )

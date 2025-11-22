"""
Dual Model Configuration for Code Generation + Visual Validation

Uses:
- Claude 4.5 Sonnet for code generation (best at coding)
- Gemini 3 Pro Preview for visual layout validation (multimodal)
"""

import os
from typing import Tuple
import litellm


class DualModelConfig:
    """Configuration for dual-model system."""
    
    # Code generation model (best at Python/Manim code)
    CODE_MODEL = "anthropic/claude-sonnet-4.5"
    
    # Visual validation model (multimodal, can see layout)
    VISUAL_MODEL = "google/gemini-3-pro-preview"
    
    @classmethod
    def get_code_model(cls) -> str:
        """Get the model for code generation."""
        return os.getenv("CODE_GEN_MODEL", cls.CODE_MODEL)
    
    @classmethod
    def get_visual_model(cls) -> str:
        """Get the model for visual validation."""
        return os.getenv("VISUAL_MODEL", cls.VISUAL_MODEL)
    
    @classmethod
    def generate_with_claude(cls, messages: list, **kwargs) -> str:
        """
        Generate code using Claude 4.5 Sonnet.
        
        Args:
            messages: Chat messages
            **kwargs: Additional parameters for litellm
        
        Returns:
            Generated code
        """
        response = litellm.completion(
            model=cls.get_code_model(),
            messages=messages,
            num_retries=2,
            **kwargs
        )
        return response.choices[0].message.content
    
    @classmethod
    def validate_with_gemini(cls, messages: list, **kwargs) -> str:
        """
        Validate layout using Gemini 3 Pro (multimodal).
        
        Args:
            messages: Chat messages (can include images)
            **kwargs: Additional parameters for litellm
        
        Returns:
            Validation feedback
        """
        response = litellm.completion(
            model=cls.get_visual_model(),
            messages=messages,
            temperature=0.3,
            **kwargs
        )
        return response.choices[0].message.content


def get_model_config() -> Tuple[str, str]:
    """
    Get current model configuration.
    
    Returns:
        Tuple of (code_model, visual_model)
    """
    return (
        DualModelConfig.get_code_model(),
        DualModelConfig.get_visual_model()
    )

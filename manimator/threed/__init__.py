"""
Manim 3D Animation Generation Module

This module provides 3D animation generation capabilities using Manim's ThreeDScene,
supporting comprehensive STEM visualizations including mathematical surfaces,
scientific models, geometric demonstrations, and 3D data visualization.
"""

__version__ = "1.0.0"
__author__ = "Manimator"

from .api.animation_generation_3d import generate_3d_animation_response
from .utils.schema_3d import ManimProcessor3D

__all__ = [
    "generate_3d_animation_response",
    "ManimProcessor3D",
]

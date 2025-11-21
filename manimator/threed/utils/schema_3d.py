"""
3D Animation Schema and Processing

Handles 3D scene rendering with Manim's ThreeDScene.
"""

import os
import subprocess
from pathlib import Path
from typing import Optional


class ManimProcessor3D:
    """Processor for rendering 3D Manim scenes"""
    
    def __init__(self):
        self.temp_dir = None
    
    def render_scene(
        self,
        scene_file: str,
        scene_name: str,
        temp_dir: str,
        quality: str = "high"
    ) -> Optional[str]:
        """
        Render a 3D Manim scene
        
        Args:
            scene_file: Path to Python file containing the scene
            scene_name: Name of the scene class to render
            temp_dir: Temporary directory for output
            quality: Rendering quality (low, medium, high, ultra)
            
        Returns:
            Path to rendered video file, or None if failed
        """
        # Quality flag mapping
        quality_flags = {
            "low": "-pql",      # 480p15
            "medium": "-pqm",   # 720p30
            "high": "-pqh",     # 1080p60
            "ultra": "-pqk"     # 4K60
        }
        
        quality_dirs = {
            "low": "480p15",
            "medium": "720p30",
            "high": "1080p60",
            "ultra": "2160p60"
        }
        
        quality_flag = quality_flags.get(quality, "-pqh")
        quality_dir = quality_dirs.get(quality, "1080p60")
        
        # Build command
        cmd = [
            "manim",
            quality_flag,
            "--media_dir",
            temp_dir,
            scene_file,
            scene_name,
        ]
        
        try:
            # Run manim
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Construct video path
            scene_file_base = Path(scene_file).stem
            video_path = os.path.join(
                temp_dir,
                "videos",
                scene_file_base,
                quality_dir,
                f"{scene_name}.mp4"
            )
            
            if os.path.exists(video_path):
                return video_path
            else:
                print(f"Video not found at expected path: {video_path}")
                return None
                
        except subprocess.CalledProcessError as e:
            print(f"Manim rendering failed: {e.stderr}")
            return None
        except Exception as e:
            print(f"Error during rendering: {str(e)}")
            return None
    
    def validate_3d_scene(self, code: str) -> bool:
        """
        Validate that the code uses ThreeDScene
        
        Args:
            code: Python code to validate
            
        Returns:
            True if code appears to use ThreeDScene, False otherwise
        """
        return "ThreeDScene" in code or "threed" in code.lower()

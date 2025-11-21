"""
ElevenLabs TTS Service for Manim Voiceover

Provides natural-sounding AI voices using ElevenLabs API.
Falls back to gTTS if ElevenLabs is unavailable or API quota is exceeded.
"""

import os
import hashlib
import requests
from pathlib import Path
from typing import Optional, Dict, Any
from manim_voiceover.services.base import SpeechService


class ElevenLabsService(SpeechService):
    """
    ElevenLabs text-to-speech service for Manim animations.
    
    Features:
    - Natural, human-like voices
    - Multiple voice options
    - Configurable voice settings
    - Audio caching to save API calls
    - Automatic fallback to gTTS
    
    Environment Variables:
        ELEVENLABS_API_KEY: Your ElevenLabs API key (required)
        ELEVENLABS_VOICE_ID: Default voice ID (optional, defaults to "Rachel")
    
    Example:
        >>> from manimator.services import ElevenLabsService
        >>> service = ElevenLabsService(voice_id="Rachel")
        >>> self.set_speech_service(service)
    """
    
    # Popular voice IDs (update these with actual ElevenLabs voice IDs)
    VOICES = {
        "Rachel": "21m00Tcm4TlvDq8ikWAM",     # Warm, educational
        "Adam": "pNInz6obpgDQGcFmaJgB",       # Professional, clear
        "Bella": "EXAVITQu4vr4xnSDxMaL",      # Engaging, narrative
        "Josh": "TxGEqnHWrfWFTfGW9XjX",       # Clear, authoritative
        "Antoni": "ErXwobaYiN019PkySvjV",     # Well-rounded, pleasant
        "Domi": "AZnzlk1XvdvUeBnXmlld",       # Strong, confident
        "Arnold": "VR6AewLTigWG4xSOukaG",     # Crisp, professional
    }
    
    def __init__(
        self,
        voice_id: Optional[str] = None,
        model_id: str = "eleven_monolingual_v1",
        stability: float = 0.6,
        similarity_boost: float = 0.8,
        style: float = 0.0,
        use_speaker_boost: bool = True,
        api_key: Optional[str] = None,
        cache_dir: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize ElevenLabs service.
        
        Args:
            voice_id: Voice ID or name (e.g., "Rachel", "Adam"). 
                     Defaults to ELEVENLABS_VOICE_ID env var or "Rachel"
            model_id: ElevenLabs model ID. Options:
                     - "eleven_monolingual_v1" (English only, fast)
                     - "eleven_multilingual_v2" (Multiple languages)
            stability: 0.0-1.0, higher = more consistent, lower = more expressive
            similarity_boost: 0.0-1.0, how closely to match the voice
            style: 0.0-1.0, style exaggeration (0 recommended for most cases)
            use_speaker_boost: Boost low-frequency audio for better clarity
            api_key: ElevenLabs API key (or from ELEVENLABS_API_KEY env var)
            cache_dir: Directory for caching audio files
        """
        super().__init__(**kwargs)
        
        # Get API key
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        if not self.api_key:
            raise ValueError(
                "ElevenLabs API key required. Set ELEVENLABS_API_KEY environment "
                "variable or pass api_key parameter."
            )
        
        # Voice configuration
        default_voice = os.getenv("ELEVENLABS_VOICE_ID", "Rachel")
        voice_id = voice_id or default_voice
        
        # Convert voice name to ID if needed
        if voice_id in self.VOICES:
            self.voice_id = self.VOICES[voice_id]
            self.voice_name = voice_id
        else:
            self.voice_id = voice_id
            self.voice_name = "Custom"
        
        self.model_id = model_id
        self.stability = stability
        self.similarity_boost = similarity_boost
        self.style = style
        self.use_speaker_boost = use_speaker_boost
        
        # Cache configuration
        if cache_dir:
            self.cache_dir = Path(cache_dir)
        else:
            self.cache_dir = Path("media/voiceover/elevenlabs")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # API configuration
        self.base_url = "https://api.elevenlabs.io/v1"
        
        # Fallback to gTTS
        self.use_fallback = False
        self.fallback_service = None
    
    def _get_cache_path(self, text: str) -> Path:
        """Get cache file path for given text"""
        # Create hash of text + settings
        cache_key = hashlib.md5(
            f"{text}_{self.voice_id}_{self.stability}_{self.similarity_boost}".encode()
        ).hexdigest()
        return self.cache_dir / f"{cache_key}.mp3"
    
    def generate_from_text(self, text: str, cache_dir: Optional[str] = None, **kwargs) -> str:
        """
        Generate speech from text using ElevenLabs API.
        
        Args:
            text: Text to convert to speech
            cache_dir: Override default cache directory
            **kwargs: Additional parameters
        
        Returns:
            Path to generated audio file
        """
        # Check cache first
        cache_path = self._get_cache_path(text)
        if cache_path.exists():
            return str(cache_path)
        
        try:
            # Call ElevenLabs API
            audio_data = self._call_api(text)
            
            # Save to cache
            with open(cache_path, 'wb') as f:
                f.write(audio_data)
            
            return str(cache_path)
            
        except Exception as e:
            print(f"⚠️  ElevenLabs API error: {e}")
            print("   Falling back to gTTS...")
            return self._use_fallback(text)
    
    def _call_api(self, text: str) -> bytes:
        """
        Call ElevenLabs API to generate speech.
        
        Args:
            text: Text to convert
        
        Returns:
            Audio data as bytes
        """
        url = f"{self.base_url}/text-to-speech/{self.voice_id}"
        
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }
        
        payload = {
            "text": text,
            "model_id": self.model_id,
            "voice_settings": {
                "stability": self.stability,
                "similarity_boost": self.similarity_boost,
                "style": self.style,
                "use_speaker_boost": self.use_speaker_boost
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code != 200:
            raise Exception(
                f"ElevenLabs API error {response.status_code}: {response.text}"
            )
        
        return response.content
    
    def _use_fallback(self, text: str) -> str:
        """
        Use gTTS as fallback when ElevenLabs fails.
        
        Args:
            text: Text to convert
        
        Returns:
            Path to generated audio file
        """
        if self.fallback_service is None:
            try:
                from manim_voiceover.services.gtts import GTTSService
                self.fallback_service = GTTSService()
            except ImportError:
                raise Exception(
                    "gTTS fallback not available. Install with: pip install gTTS"
                )
        
        return self.fallback_service.generate_from_text(text)
    
    def get_available_voices(self) -> Dict[str, str]:
        """
        Get dict of available voice names and IDs.
        
        Returns:
            Dictionary mapping voice names to IDs
        """
        return self.VOICES.copy()
    
    def get_voice_info(self) -> Dict[str, Any]:
        """
        Get information about current voice configuration.
        
        Returns:
            Dictionary with voice settings
        """
        return {
            "voice_name": self.voice_name,
            "voice_id": self.voice_id,
            "model_id": self.model_id,
            "stability": self.stability,
            "similarity_boost": self.similarity_boost,
            "style": self.style,
            "use_speaker_boost": self.use_speaker_boost
        }


# Convenience function for quick setup
def create_elevenlabs_service(
    voice: str = "Rachel",
    educational: bool = True
) -> ElevenLabsService:
    """
    Create ElevenLabs service with preset configurations.
    
    Args:
        voice: Voice name (Rachel, Adam, Bella, etc.)
        educational: If True, use settings optimized for educational content
    
    Returns:
        Configured ElevenLabsService
    
    Example:
        >>> service = create_elevenlabs_service(voice="Rachel", educational=True)
        >>> self.set_speech_service(service)
    """
    if educational:
        # Educational preset: stable, clear, professional
        return ElevenLabsService(
            voice_id=voice,
            stability=0.6,
            similarity_boost=0.8,
            style=0.0
        )
    else:
        # Expressive preset: more dynamic, engaging
        return ElevenLabsService(
            voice_id=voice,
            stability=0.4,
            similarity_boost=0.75,
            style=0.2
        )

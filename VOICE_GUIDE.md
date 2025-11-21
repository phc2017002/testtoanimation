# ElevenLabs Voice Integration Guide

## Overview

The voice system has been upgraded from robotic gTTS (Google Text-to-Speech) to natural-sounding ElevenLabs AI voices for professional-quality narration in both 2D and 3D animations.

## ✨ What Changed

**Before (gTTS):**
- Robotic, mechanical voice
- Limited emotional range
- Poor pronunciation of technical terms
- Basic quality

**After (ElevenLabs):**
- Natural, human-like voice
- Professional voice actors
- Clear pronunciation
- Context-aware intonation
- Multiple voice personalities

## 🎤 Available Voices

| Voice | Personality | Best For | Use Case |
|-------|-------------|----------|----------|
| **Rachel** | Warm, educational | Teaching, explanations | Mathematical concepts, tutorials |
| **Adam** | Professional, clear | Technical content | Scientific explanations, formal presentations |
| **Bella** | Engaging, narrative | Storytelling | Complex visualizations, engaging content |
| **Josh** | Clear, authoritative | Scientific content | Physics, chemistry, formal education |
| **Antoni** | Well-rounded, pleasant | General use | Versatile, any topic |
| **Domi** | Strong, confident | Dynamic content | Action-oriented, energetic topics |
| **Arnold** | Crisp, professional | Technical | Programming, engineering |

## 🚀 Quick Start

### Setup

1. **API Key is already configured** in `.env`:
   ```bash
   ELEVENLABS_API_KEY=sk_354da574066d7408834f11841dca954ef37764c92703bc99
   ELEVENLABS_VOICE_ID=Rachel
   ```

2. **No additional installation needed** - the service is ready to use!

### Basic Usage

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class MyAnimation(VoiceoverScene):
    def construct(self):
        # Use default voice (Rachel)
        self.set_speech_service(ElevenLabsService())
        
        with self.voiceover(text="Hello! This is a natural-sounding voice"):
            title = Text("ElevenLabs Demo")
            self.play(Write(title))
```

### Choose Different Voice

```python
# Use Adam for professional tone
self.set_speech_service(ElevenLabsService(voice_id="Adam"))

# Use Bella for engaging narration
self.set_speech_service(ElevenLabsService(voice_id="Bella"))

# Use Josh for scientific content
self.set_speech_service(ElevenLabsService(voice_id="Josh"))
```

### Custom Voice Settings

```python
# Fine-tune voice characteristics
self.set_speech_service(
    ElevenLabsService(
        voice_id="Rachel",
        stability=0.7,        # Higher = more consistent (0.0-1.0)
        similarity_boost=0.8, # How closely to match voice (0.0-1.0)
        style=0.0             # Style exaggeration (0.0-1.0)
    )
)
```

### Convenience Function

```python
from manimator.services.elevenlabs_service import create_elevenlabs_service

# Educational preset (stable, clear)
service = create_elevenlabs_service(voice="Rachel", educational=True)
self.set_speech_service(service)

# Expressive preset (dynamic, engaging)
service = create_elevenlabs_service(voice="Bella", educational=False)
self.set_speech_service(service)
```

## 🎓 For 3D Animations

The exact same syntax works for 3D animations:

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class My3DAnimation(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        
        with self.voiceover(text="Let's explore this 3D structure"):
            sphere = Sphere()
            self.play(Create(sphere))
```

## 💾 Caching

**Audio files are automatically cached** to save API calls and improve performance:

- Location: `media/voiceover/elevenlabs/`
- Format: MP3
- Naming: Hash of text + settings
- Reuse: Same text + settings = cached file used

**Benefits:**
- Faster re-renders
- Lower API costs
- Consistent voice across renders

## 🔄 Fallback to gTTS

If ElevenLabs fails (API error, quota exceeded, network issue), the system automatically falls back to gTTS:

```
⚠️  ElevenLabs API error: Quota exceeded
   Falling back to gTTS...
```

This ensures your animations always complete, even if there's an API issue.

## 📊 Voice Settings Guide

### Stability (0.0 - 1.0)

- **0.3-0.4**: Very expressive, dynamic (storytelling)
- **0.5-0.6**: Balanced (recommended for most content) ✅
- **0.7-0.8**: Very stable (technical, formal)

### Similarity Boost (0.0 - 1.0)

- **0.5-0.7**: Looser match, more variety
- **0.75-0.85**: Recommended range ✅
- **0.9-1.0**: Very tight match to original voice

### Style (0.0 - 1.0)

- **0.0**: Neutral (recommended for education) ✅
- **0.2-0.4**: Slight emphasis
- **0.5-1.0**: Strong style exaggeration

## 🧪 Testing

### Test Voice Quality

```python
# Create test_voice.py
from manimator.services import ElevenLabsService

service = ElevenLabsService(voice_id="Rachel")
audio_path = service.generate_from_text(
    "This is a test of the ElevenLabs voice system. "
    "Notice the natural intonation and clear pronunciation of technical terms like Manim and ThreeDScene."
)
print(f"Audio saved to: {audio_path}")

# Play the audio file to hear the quality
```

### Compare Voices

```bash
# Render same animation with different voices
manim -pql my_scene.py MyScene  # Uses default Rachel
# Edit to use Adam
manim -pql my_scene.py MyScene  # Compare quality
```

## 🎯 Best Practices

1. **Choose appropriate voice** for content type
   - Educational → Rachel, Adam
   - Scientific → Josh, Arnold
   - Engaging → Bella, Antoni

2. **Use educational preset** for most animations:
   ```python
   service = create_elevenlabs_service(voice="Rachel", educational=True)
   ```

3. **Keep narration natural**:
   - Write conversationally
   - Use contractions ("let's" not "let us")
   - Include pauses with punctuation

4. **Test voice before long renders**:
   - Render 10-second sample first
   - Verify voice quality
   - Then render full animation

5. **Monitor API usage**:
   - Check ElevenLabs dashboard
   - Use caching effectively
   - Consider character limits

## 📈 API Usage

**Free Tier:**
- 10,000 characters/month
- ~2-3 minutes of narration per month

**Starter ($5/month):**
- 30,000 characters/month
- ~6-10 minutes of narration

**Creator ($22/month):**
- 100,000 characters/month
- ~20-30 minutes of narration

**Tip:** Average 5-minute animation ≈ 3,000-5,000 characters

## 🔧 Troubleshooting

### API Key Error
```python
ValueError: ElevenLabs API key required
```
**Solution:** Check `.env` file has `ELEVENLABS_API_KEY` set

### Quota Exceeded
```
⚠️  ElevenLabs API error: Quota exceeded
```
**Solution:** System automatically falls back to gTTS. Upgrade plan or wait for quota reset.

### Network Error
```
⚠️  ElevenLabs API error: Connection timeout
```
**Solution:** Check internet connection. System will use gTTS fallback.

### Voice Not Found
```python
# If using custom voice ID
ElevenLabsService(voice_id="custom_id_here")
```
**Solution:** Use predefined names (Rachel, Adam, etc.) or valid ElevenLabs voice ID

## 🎬 Complete Example

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class ElectronOrbitals(VoiceoverScene):
    def construct(self):
        # Use Josh for scientific content
        self.set_speech_service(
            ElevenLabsService(
                voice_id="Josh",
                stability=0.6,  # Balanced
                similarity_boost=0.8
            )
        )
        
        # Introduction
        with self.voiceover(
            text="Welcome to this visualization of electron orbitals. "
                 "We'll explore how electrons distribute around atomic nuclei."
        ):
            title = Text("Electron Orbitals", font_size=48)
            self.play(Write(title))
            self.wait(1)
            self.play(FadeOut(title))
        
        # Show atom
        with self.voiceover(
            text="Here we see a hydrogen atom with its single electron "
                 "occupying the first orbital shell."
        ):
            nucleus = Dot(color=RED, radius=0.2)
            electron = Dot(color=BLUE, radius=0.1)
            orbit = Circle(radius=2, color=WHITE)
            
            self.play(Create(nucleus))
            self.play(Create(orbit), Create(electron.move_to(orbit.point_at_angle(0))))
        
        # Animate orbit
        with self.voiceover(
            text="The electron moves around the nucleus in its orbital path."
        ):
            self.play(
                MoveAlongPath(electron, orbit),
                rate_func=linear,
                run_time=3
            )
```

---

**The voice system is now production-ready with professional-quality AI narration!** 🎉

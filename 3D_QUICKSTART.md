# 3D Animation System - Quick Test

Quick test script to verify the 3D animation system is working.

## Test 1: Simple 3D Sphere

```bash
# Create a test file
cat > test_3d_simple.py << 'EOF'
from manim import *

class SimpleSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        sphere = Sphere(radius=1, resolution=(20, 20))
        sphere.set_color_by_gradient(BLUE, GREEN, YELLOW)
        
        self.play(Create(sphere))
        self.play(Rotate(sphere, angle=2*PI, axis=UP, run_time=3))
        self.wait()
EOF

# Render it
manim -pql test_3d_simple.py SimpleSphere
```

## Test 2: Start 3D API Server

```bash
# Start the server
~/.local/bin/poetry run python api_server_3d.py

# Server will run on port 8001
# Visit: http://localhost:8001/docs
```

## Test 3: Create 3D Animation via API

```bash
# Test endpoint
curl -X POST http://localhost:8001/api/3d-videos \
  -H "Content-Type: application/json" \  -d '{
    "prompt": "Create a rotating cube with coordinate axes in 3D",
    "category": "geometric",
    "quality": "low"
  }'
```

## Test 4: Python Client

```python
import requests
import time

# Create job
response = requests.post("http://localhost:8001/api/3d-videos", json={
    "prompt": "Visualize a 3D sine wave surface with rotating camera",
    "category": "mathematical",
    "quality": "low"
})

job_id = response.json()["job_id"]
print(f"Job created: {job_id}")

# Check status
while True:
    status = requests.get(f"http://localhost:8001/api/3d-jobs/{job_id}").json()
    print(f"{status['progress']['percentage']}%: {status['progress']['message']}")
    
    if status['status'] in ['completed', 'failed']:
        break
    
    time.sleep(3)

# Download if successful
if status['status'] == 'completed':
    video = requests.get(f"http://localhost:8001/api/3d-videos/{job_id}")
    with open("test_3d.mp4", "wb") as f:
        f.write(video.content)
    print("✅ Video downloaded: test_3d.mp4")
```

## What to Expect

✅ Server starts on port 8001  
✅ Real-time progress logging in terminal  
✅ 3D code generation with ThreeDScene  
✅ Camera controls and 3D rendering  
✅ Category-specific prompts (mathematical, scientific, geometric, data)  

## Troubleshooting

### Import Error
```bash
# Make sure you're in the project directory
cd /Users/aniketpal/Downloads/manimator
```

### Port in Use
```bash
# Check if something else is using port 8001
lsof -ti:8001

# Use different port if needed
uvicorn api_server_3d:app --port 8002
```

### 3D Rendering Fails
```bash
# Test Manim 3D directly
manim -pql test_3d_simple.py SimpleSphere

# Check OpenGL support
python -c "from manim import *; print('3D support OK')"
```

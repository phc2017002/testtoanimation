# Manim 3D Video Generation API

A comprehensive 3D animation generation system built on Manim's ThreeDScene, supporting all STEM visualizations.

## 🎯 Features

- 🧮 **Mathematical Visualizations**: Surfaces, vector fields, calculus in 3D
- 🔬 **Scientific Models**: Molecules, physics simulations, crystal structures
- 📐 **Geometric Demonstrations**: Shapes, transformations, spatial relationships
- 📊 **3D Data Visualization**: Scatter plots, surfaces, network graphs

## 🚀 Quick Start

### 1. Start the 3D Server (Port 8001)

```bash
cd /Users/aniketpal/Downloads/manimator
~/.local/bin/poetry run python api_server_3d.py

# Server runs on: http://localhost:8001
# Docs at: http://localhost:8001/docs
```

### 2. Create a 3D Animation

```python
import requests

response = requests.post("http://localhost:8001/api/3d-videos", json={
    "prompt": "Create a rotating DNA double helix in 3D with labeled base pairs",
    "quality": "high",
    "category": "scientific"
})

job_id = response.json()["job_id"]
print(f"Job created: {job_id}")
```

### 3. Check Status & Download

```python
# Check status
status = requests.get(f"http://localhost:8001/api/3d-jobs/{job_id}").json()
print(f"Status: {status['status']}")

# Download when complete
if status['status'] == 'completed':
    video = requests.get(f"http://localhost:8001/api/3d-videos/{job_id}")
    with open("dna.mp4", "wb") as f:
        f.write(video.content)
```

## 📋 STEM Categories

### Mathematical
- 3D function surfaces
- Vector fields
- Parametric surfaces
- Calculus visualizations

### Scientific
- Molecular structures
- Physics simulations  
- Orbital mechanics
- Electromagnetic fields

### Geometric
- 3D shapes & transformations
- Rotation matrices
- Cross/dot products
- Symmetry groups

### Data
- 3D scatter plots
- Surface plots from data
- Network graphs in 3D
- Animated data evolution

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/3d-videos` | POST | Create 3D video job |
| `/api/3d-jobs/{id}` | GET | Check job status |
| `/api/3d-videos/{id}` | GET | Download video |
| `/api/3d-jobs` | GET | List all jobs |
| `/health` | GET | Server health |

## 💡 Example Prompts

### 1. Mathematical Surface
```json
{
  "prompt": "Visualize the surface z = sin(x) * cos(y) in 3D with rotating camera",
  "category": "mathematical",
  "quality": "high"
}
```

### 2. Molecular Structure
```json
{
  "prompt": "Create a 3D animation of a water molecule showing electron orbitals",
  "category": "scientific",
  "quality": "high"
}
```

### 3. Geometric Demo
```json
{
  "prompt": "Show a cube rotating through all axes with transformation matrices",
  "category": "geometric",
  "quality": "high"
}
```

### 4. Data Visualization
```json
{
  "prompt": "Create a 3D scatter plot showing correlation between three variables",
  "category": "data",
  "quality": "high"
}
```

## 🎬 Quality Levels

| Quality | Resolution | FPS | Use Case |
|---------|------------|-----|----------|
| low | 480p | 15 | Quick previews |
| medium | 720p | 30 | Testing |
| **high** | 1080p | 60 | **Production** ✅ |
| ultra | 4K | 60 | High-end |

## 🔧 Python Client

```python
import requests
import time

class Manim3DClient:
    def __init__(self, base_url="http://localhost:8001"):
        self.base_url = base_url
    
    def create_video(self, prompt, category="general", quality="high"):
        response = requests.post(
            f"{self.base_url}/api/3d-videos",
            json={
                "prompt": prompt,
                "category": category,
                "quality": quality
            }
        )
        return response.json()["job_id"]
    
    def get_status(self, job_id):
        response = requests.get(f"{self.base_url}/api/3d-jobs/{job_id}")
        return response.json()
    
    def wait_for_completion(self, job_id):
        while True:
            status = self.get_status(job_id)
            print(f"{status['progress']['message']}")
            
            if status['status'] in ['completed', 'failed']:
                return status
            
            time.sleep(5)
    
    def download_video(self, job_id, output_path):
        response = requests.get(f"{self.base_url}/api/3d-videos/{job_id}")
        with open(output_path, 'wb') as f:
            f.write(response.content)

# Usage
client = Manim3DClient()
job_id = client.create_video(
    prompt="Visualize a 3D vector field",
    category="mathematical"
)
client.wait_for_completion(job_id)
client.download_video(job_id, "vector_field.mp4")
```

## 🛠️ Development

### Run Both Servers

```bash
# Terminal 1: 2D Server (port 8000)
poetry run python api_server.py

# Terminal 2: 3D Server (port 8001)
poetry run python api_server_3d.py
```

### Test 3D Endpoint

```bash
curl -X POST http://localhost:8001/api/3d-videos \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create a rotating sphere with coordinate axes",
    "category": "geometric",
    "quality": "low"
  }'
```

## 📚 Architecture

```
manimator/
├── threed/                    # 3D animation module
│   ├── api/
│   │   ├── animation_generation_3d.py  # Code generation
│   │   └── prompts_3d.py               # System prompts
│   └── utils/
│       └── schema_3d.py                # 3D rendering
├── api_server.py             # 2D server (port 8000)
└── api_server_3d.py          # 3D server (port 8001)
```

## 🎓 Learning Resources

The 3D system uses Manim's ThreeDScene which provides:

- **Camera Controls**: `set_camera_orientation()`, `move_camera()`
- **3D Objects**: `Sphere()`, `Cube()`, `Surface()`, `Arrow3D()`
- **3D Axes**: `ThreeDAxes()`
- **Camera Rotation**: `begin_ambient_camera_rotation()`

## 📖 Documentation

- Interactive API Docs: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc

## 🤝 Integration with 2D System

Both APIs can run simultaneously:
- **2D Animations**: Port 8000 (`/api/videos`)
- **3D Animations**: Port 8001 (`/api/3d-videos`)

Choose based on your needs:
- Use 2D for diagrams, charts, algorithms
- Use 3D for spatial concepts, molecules, surfaces

## 🐛 Troubleshooting

### 3D Rendering Issues
```bash
# Check if 3D features work
manim -pql test_3d.py TestScene3D

# Verify camera supports 3D
# Some systems may have OpenGL limitations
```

### Port Already in Use
```bash
# Use different port
uvicorn api_server_3d:app --port 8002
```

## 📝 License

Same as Manimator project

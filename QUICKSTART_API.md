# FastAPI Video Generation API - Quick Start Guide

## 🚀 What You Got

A **complete production-ready API** for generating Manim videos from text prompts!

### Files Created:
1. **`api_server.py`** - FastAPI server with async job processing
2. **`api_client.py`** - Python client library + CLI tool
3. **`API_README.md`** - Full documentation
4. **`examples_api.py`** - Usage examples

---

## ⚡ Quick Start (30 seconds)

### 1. Start Server
```bash
cd /Users/aniketpal/Downloads/manimator
~/.local/bin/poetry run python api_server.py
```

Server runs at: **http://localhost:8000**  
Docs at: **http://localhost:8000/docs**

### 2. Create Video (Python)
```python
from api_client import ManimVideoClient, QualityLevel

client = ManimVideoClient()

# Create video
job = client.create_video(
    prompt="Create a 1-minute animation explaining recursion",
    quality=QualityLevel.HIGH
)

print(f"Job ID: {job['job_id']}")
```

### 3. Or Use Command Line
```bash
# Create video
python api_client.py generate \
  --prompt "Explain binary search with animations" \
  --output output.mp4 \
  --quality high
```

---

## 📡 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `POST` | `/api/videos` | Create video job |
| `GET` | `/api/jobs/{id}` | Check status |
| `GET` | `/api/videos/{id}` | Download video |
| `GET` | `/api/jobs` | List all jobs |
| `DELETE` | `/api/jobs/{id}` | Delete job |
| `GET` | `/health` | Server health |

---

## 🎬 Complete Example

```python
from api_client import ManimVideoClient

client = ManimVideoClient()

# Progress callback
def show_progress(status):
    pct = status['progress']['percentage']
    msg = status['progress']['message']
    print(f"[{pct}%] {msg}")

# Generate & download
client.generate_and_download(
    prompt="Create 2-min animation about quicksort",
    output_path="quicksort.mp4",
    progress_callback=show_progress
)

print("Done! Video saved to quicksort.mp4")
```

---

## 🔧 Quality Levels

- `low` - 480p15 (fast, for testing)
- `medium` - 720p30
- **`high`** - 1080p60 (recommended) ✅
- `ultra` - 4K60 (slow)

---

## 📚 Full Documentation

See **`API_README.md`** for:
- Detailed API reference
- JavaScript/TypeScript examples
- Production deployment
- Docker setup
- Troubleshooting

---

## 🧪 Test It

```bash
# Run example scripts
python examples_api.py

# Or test specific example
python -c "from examples_api import example_5_health_check; example_5_health_check()"
```

---

## 🎯 Features

✅ Async job processing  
✅ Real-time progress tracking  
✅ Multiple quality levels  
✅ Automatic file management  
✅ Job history & cleanup  
✅ Auto-generated API docs  
✅ Python client library  
✅ CLI tool  
✅ Production-ready  

---

**That's it!** You now have a complete API for video generation. 🎉

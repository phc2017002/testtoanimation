# Manim Video Generation API

A production-ready FastAPI server for generating educational animation videos from text prompts using Manim.

## Features

- 🚀 **Async Job Processing**: Background video generation with job queue
- 📊 **Status Tracking**: Real-time progress monitoring
- 🎬 **Multiple Quality Levels**: Low (480p), Medium (720p), High (1080p), Ultra (4K)
- 📁 **File Management**: Automatic file organization and cleanup
- 🔍 **Job History**: List and manage all generation jobs
- 📚 **Auto-generated Docs**: Interactive API documentation
- ⚡ **REST API**: Simple HTTP endpoints for all operations

## Installation

```bash
# Navigate to manimator directory
cd /Users/aniketpal/Downloads/manimator

# Install dependencies (if not already done)
~/.local/bin/poetry install

# Ensure you have .env file with API key
echo "GEMINI_API_KEY=your_api_key_here" >> .env
```

## Quick Start

### 1. Start the Server

```bash
# Start the API server
~/.local/bin/poetry run python api_server.py

# Server will start at: http://localhost:8000
# API Docs at: http://localhost:8000/docs
```

### 2. Create a Video

```bash
# Using curl
curl -X POST "http://localhost:8000/api/videos" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create a 2-minute animation explaining binary search with visualizations",
    "quality": "high"
  }'

# Response:
# {
#   "job_id": "abc-123-def-456",
#   "status": "pending",
#   "message": "Job created successfully",
#   "created_at": "2025-11-21T14:00:00"
# }
```

### 3. Check Status

```bash
# Get job status
curl "http://localhost:8000/api/jobs/abc-123-def-456"

# Response includes:
# - status: pending | generating_code | rendering | completed | failed
# - progress: { stage, percentage, message }
# - video_url: (when completed)
```

### 4. Download Video

```bash
# Download completed video
curl "http://localhost:8000/api/videos/abc-123-def-456" \
  -o my_video.mp4
```

## API Endpoints

### `POST /api/videos`
Create a new video generation job

**Request:**
```json
{
  "prompt": "Your detailed animation prompt",
  "quality": "high",  // low | medium | high | ultra
  "scene_name": "MyScene"  // optional
}
```

**Response:**
```json
{
  "job_id": "uuid",
  "status": "pending",
  "message": "Job created successfully",
  "created_at": "ISO timestamp"
}
```

### `GET /api/jobs/{job_id}`
Get job status and progress

**Response:**
```json
{
  "job_id": "uuid",
  "status": "rendering",
  "progress": {
    "stage": "rendering",
    "percentage": 60,
    "message": "Rendering video..."
  },
  "created_at": "ISO timestamp",
  "updated_at": "ISO timestamp",
  "video_url": "/api/videos/uuid",  // when completed
  "duration": 120.5  // video duration in seconds
}
```

### `GET /api/videos/{job_id}`
Download the generated video file

Returns: MP4 video file

### `GET /api/jobs`
List all jobs (most recent first)

**Query Parameters:**
- `limit`: Max number of jobs to return (default: 50)

### `DELETE /api/jobs/{job_id}`
Delete a job and its files

### `GET /health`
Health check endpoint with statistics

## Quality Levels

| Quality | Resolution | FPS | Use Case | Render Time |
|---------|------------|-----|----------|-------------|
| `low` | 480p | 15 | Quick previews | Fast |
| `medium` | 720p | 30 | Testing | Moderate |
| `high` | 1080p | 60 | **Production** ✅ | Slow |
| `ultra` | 4K | 60 | High-end | Very Slow |

## Python Client Examples

### Basic Example

```python
import requests
import time

# 1. Create video job
response = requests.post("http://localhost:8000/api/videos", json={
    "prompt": """
    Create a 3-minute animation explaining how HTTP works:
    - Show client-server communication
    - Animate request/response flow
    - Display HTTP methods (GET, POST, etc.)
    - Include status codes visualization
    """,
    "quality": "high"
})

job_id = response.json()["job_id"]
print(f"Job created: {job_id}")

# 2. Poll for completion
while True:
    status = requests.get(f"http://localhost:8000/api/jobs/{job_id}").json()
    
    print(f"Status: {status['status']} - {status['progress']['message']}")
    
    if status['status'] == 'completed':
        print(f"✅ Video ready! Duration: {status['duration']}s")
        break
    elif status['status'] == 'failed':
        print(f"❌ Failed: {status['error']}")
        break
    
    time.sleep(5)  # Check every 5 seconds

# 3. Download video
video = requests.get(f"http://localhost:8000/api/videos/{job_id}")
with open("output.mp4", "wb") as f:
    f.write(video.content)

print("Video downloaded: output.mp4")
```

### Async Example (Python 3.7+)

```python
import httpx
import asyncio

async def generate_video(prompt: str):
    async with httpx.AsyncClient() as client:
        # Create job
        response = await client.post(
            "http://localhost:8000/api/videos",
            json={"prompt": prompt, "quality": "high"}
        )
        job_id = response.json()["job_id"]
        
        # Wait for completion
        while True:
            response = await client.get(
                f"http://localhost:8000/api/jobs/{job_id}"
            )
            status = response.json()
            
            if status['status'] in ['completed', 'failed']:
                return status
            
            await asyncio.sleep(5)

# Run
result = asyncio.run(generate_video("Your prompt here"))
```

## JavaScript/TypeScript Client

```javascript
// Create video
const response = await fetch('http://localhost:8000/api/videos', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    prompt: 'Create a 2-minute animation about recursion',
    quality: 'high'
  })
});

const { job_id } = await response.json();

// Poll for status
const checkStatus = async () => {
  const res = await fetch(`http://localhost:8000/api/jobs/${job_id}`);
  const status = await res.json();
  
  console.log(`${status.status}: ${status.progress.message}`);
  
  if (status.status === 'completed') {
    // Download video
    window.location.href = status.video_url;
  } else if (status.status !== 'failed') {
    setTimeout(checkStatus, 5000);
  }
};

checkStatus();
```

## Configuration

Edit `api_server.py` to customize:

```python
class Config:
    BASE_DIR = Path(__file__).parent
    JOBS_DIR = BASE_DIR / "jobs"
    VIDEOS_DIR = BASE_DIR / "media" / "videos"
    MAX_JOB_AGE_DAYS = 7  # Auto-cleanup old jobs
```

## Development

### Running with Auto-reload

```bash
~/.local/bin/poetry run uvicorn api_server:app --reload --host 0.0.0.0 --port 8000
```

### Testing

```bash
# Test endpoints
curl http://localhost:8000/health

# Create test job
curl -X POST http://localhost:8000/api/videos \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test animation", "quality": "low"}'
```

## Production Deployment

### Using Gunicorn (Recommended)

```bash
# Install gunicorn
~/.local/bin/poetry add gunicorn

# Run with multiple workers
gunicorn api_server:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

### Using Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libcairo2 \
    libpango-1.0-0 \
    sox

# Install poetry
RUN pip install poetry

# Copy project files
COPY . .

# Install dependencies
RUN poetry install

# Expose port
EXPOSE 8000

# Run server
CMD ["poetry", "run", "python", "api_server.py"]
```

## Troubleshooting

### Server won't start
```bash
# Check if port 8000 is in use
lsof -ti:8000

# Use different port
uvicorn api_server:app --port 8080
```

### Jobs failing
```bash
# Check logs in jobs/*.json files
cat jobs/<job_id>.json

# Test Manim directly
manim -pql test_scene.py TestScene
```

### Videos not generating
```bash
# Verify dependencies
ffmpeg -version
manim --version

# Check API key
cat .env | grep API_KEY
```

## API Documentation

Once the server is running, visit:
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## License

Same as Manimator project

## Support

For issues or questions, create an issue on the GitHub repository.

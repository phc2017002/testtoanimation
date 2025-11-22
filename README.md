# Text to Animation

Transform any text prompt into stunning mathematical and educational animations powered by AI and the [Manim](https://github.com/ManimCommunity/manim) engine.

## 🎯 What is Text to Animation?

This tool converts natural language descriptions into beautiful, professional-quality animations. Simply describe what you want to visualize - whether it's a mathematical concept, scientific principle, or educational explanation - and the system generates an animated video using the powerful Manim library.

### ✨ Key Features

- **AI-Powered Animation Generation**: Converts text prompts into Manim code automatically
- **Voiceover Support**: Generates animations with synchronized AI voiceovers
- **Mathematical Equations**: Renders beautiful LaTeX equations and mathematical visualizations
- **FastAPI Backend**: RESTful API for programmatic access
- **Gradio Interface**: User-friendly web interface for easy interaction
- **Flexible LLM Support**: Works with various AI models (Gemini, DeepSeek, Claude, etc.)

## 📋 System Requirements & Dependencies

### System Dependencies

This project is built on the [Manim](https://github.com/ManimCommunity/manim) engine, which requires the following system dependencies:

#### macOS
```bash
# Install basic dependencies
brew install cairo ffmpeg pango pkg-config

# Install LaTeX (required for mathematical equations and MathTex)
brew install --cask basictex

# After installation, update PATH in your current terminal:
eval "$(/usr/libexec/path_helper)"

# Install additional LaTeX packages that Manim needs
sudo tlmgr update --self
sudo tlmgr install latex-bin amsmath amsfonts amssymb babel-english cbfonts-fd cm-super ctex dvipng environ filehook float fontspec frcursive fundus-calligra jknapltx latexmk metalogo microtype ms physics rsfs scheme-infraonly setspace standalone tools unicode-math xcolor
```

**Note:** After installing BasicTeX, you may need to restart your terminal or run `eval "$(/usr/libexec/path_helper)"` to update your PATH. The `tlmgr` commands require sudo password.

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
```

#### Windows
Install the following:
- [FFmpeg](https://ffmpeg.org/download.html)
- [Cairo](https://www.cairographics.org/download/)
- [Pango](https://pango.gnome.org/)

For detailed Manim installation instructions, see the [official documentation](https://docs.manim.community/en/stable/installation.html).

### Python Dependencies

This project uses [Poetry](https://python-poetry.org/) for dependency management. The key dependencies include:

**Core Dependencies:**
- `python` >= 3.11, < 3.13
- `manim` ^0.18.1 - Animation engine
- `manim-voiceover[gtts]` ^0.3.7 - Voiceover support with Google Text-to-Speech

**API & Web Framework:**
- `fastapi` ^0.115.6 - REST API framework
- `uvicorn` ^0.34.0 - ASGI server
- `gradio` ^5.9.1 - Web interface

**AI & LLM Integration:**
- `litellm` ^1.56.10 - Unified LLM API interface
- `google-genai` ^1.51.0 - Google Gemini integration

**Utilities:**
- `python-dotenv` 0.21.0 - Environment variable management
- `python-multipart` ^0.0.20 - File upload support
- `tenacity` ^9.0.0 - Retry logic
- `pypdf2` ^3.0.1 - PDF processing
- `setuptools` ^80.9.0 - Build tools

## 🚀 Installation

### 1. Install Poetry

Download and install Poetry from [here](https://python-poetry.org/docs/#installing-with-the-official-installer):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. Clone the Repository

```bash
git clone https://github.com/phc2017002/testtoanimation.git
cd testtoanimation
```

### 3. Install Dependencies

```bash
poetry install
```

### 4. Activate the Virtual Environment

For Poetry 2.0+:
```bash
poetry env activate
```

For older versions:
```bash
poetry shell
```

### 5. Set Up Environment Variables

Create a `.env` file in the root directory with your API keys:

```env
# Required: At least one LLM API key
GEMINI_API_KEY=your_gemini_api_key_here
# Or use other providers:
# OPENAI_API_KEY=your_openai_api_key
# ANTHROPIC_API_KEY=your_anthropic_api_key
# DEEPSEEK_API_KEY=your_deepseek_api_key

# Optional: Model configuration (defaults to Gemini)
# LLM_MODEL=gemini/gemini-1.5-flash
```

## 💻 Usage

### Running the FastAPI Server

Start the REST API server:

```bash
poetry run app
```

Visit `http://localhost:8000/docs` to open the interactive Swagger UI documentation.

### Running the Gradio Interface

Start the web interface:

```bash
poetry run gradio-app
```

Open your browser and navigate to `http://localhost:7860`.

### API Example

Generate an animation from a text prompt:

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Explain the Pythagorean theorem with a visual proof"}' \
     --output animation.mp4 \
     http://localhost:8000/generate-animation
```

## 🔧 Configuration

### Changing AI Models

The system supports multiple LLM providers through [LiteLLM](https://docs.litellm.ai/docs/providers). Set your preferred model in the `.env` file:

```env
LLM_MODEL=gemini/gemini-2.0-flash-exp
# or
LLM_MODEL=anthropic/claude-3-5-sonnet-20241022
# or
LLM_MODEL=deepseek/deepseek-chat
```

### Customizing System Prompts

To modify how the AI generates animations, edit the system prompts in:
- `manimator/utils/system_prompts.py`

### Adjusting Few-Shot Examples

Improve generation quality by modifying examples in:
- `manimator/few_shot/few_shot_prompts.py`

## 🐳 Docker

Build and run the application using Docker:

### Build the Docker Image

```bash
docker build -t texttoanimation .
```

### Run FastAPI Server

```bash
docker run -p 8000:8000 texttoanimation
```

### Run Gradio Interface

```bash
docker run -p 7860:7860 texttoanimation
```

## 📚 API Endpoints

### Generate Animation
- **Endpoint**: `/generate-animation`
- **Method**: POST
- **Description**: Generates an animated video from a text prompt
- **Input**: `{"prompt": "Your description here"}`
- **Output**: MP4 video file

### Health Check
- **Endpoint**: `/health-check`
- **Method**: GET
- **Description**: Check API status

For complete API documentation, visit `/docs` after starting the server.

## 🎨 Example Prompts

Try these example prompts to see what the system can create:

- "Create an animation explaining how neural networks learn"
- "Visualize the Fourier transform with examples"
- "Show how gradient descent works in machine learning"
- "Explain quantum entanglement with visual demonstrations"
- "Demonstrate the concept of limits in calculus"

## 🙏 Acknowledgements

This project builds upon the incredible work of:
- [Manim Community](https://www.manim.community/) and [3Blue1Brown](https://github.com/3b1b/manim) for the animation engine
- Original [manimator](https://github.com/HyperCluster-Tech/manimator) project developers: [Samarth P](https://github.com/samarth777), [Vyoman Jain](https://github.com/VyoJ), [Shiva Golugula](https://github.com/Shiva4113), and [M Sai Sathvik](https://github.com/User-LazySloth)

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more information.

The project uses the [Manim engine](https://github.com/ManimCommunity/manim), which is double-licensed under the MIT license, with copyright by 3blue1brown LLC and Manim Community Developers.

## 📧 Contact

For inquiries, please open an issue on GitHub.

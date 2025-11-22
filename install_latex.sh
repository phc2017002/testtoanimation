#!/bin/bash

# LaTeX Installation Script for macOS
# This script installs BasicTeX and required LaTeX packages for Manim

set -e

echo "🔧 Installing LaTeX for Manim..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew is not installed. Please install it first:"
    echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
fi

# Install BasicTeX
echo "📦 Installing BasicTeX..."
brew install --cask basictex

# Update PATH
echo "🔄 Updating PATH..."
eval "$(/usr/libexec/path_helper)"

# Wait a moment for installation to complete
sleep 2

# Check if tlmgr is available
if ! command -v tlmgr &> /dev/null; then
    echo "⚠️  tlmgr not found in PATH. Please restart your terminal and run:"
    echo "   eval \"\$(/usr/libexec/path_helper)\""
    echo "   Then run this script again, or manually run the tlmgr commands below."
    exit 1
fi

# Update tlmgr
echo "📥 Updating TeX Live Manager..."
sudo tlmgr update --self

# Install required LaTeX packages
echo "📚 Installing required LaTeX packages for Manim..."
sudo tlmgr install \
    latex-bin \
    amsmath \
    amsfonts \
    amssymb \
    babel-english \
    cbfonts-fd \
    cm-super \
    ctex \
    dvisvgm \
    dvipng \
    environ \
    filehook \
    float \
    fontspec \
    frcursive \
    fundus-calligra \
    jknapltx \
    latexmk \
    metalogo \
    microtype \
    ms \
    physics \
    preview \
    rsfs \
    scheme-infraonly \
    setspace \
    standalone \
    tools \
    unicode-math \
    xcolor

echo "✅ LaTeX installation complete!"
echo ""
echo "To verify installation, run:"
echo "   pdflatex --version"
echo "   which pdflatex"


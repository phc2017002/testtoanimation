#!/bin/bash
# Quick fix for dvisvgm installation

eval "$(/usr/libexec/path_helper)"

echo "Installing dvisvgm..."
sudo tlmgr install dvisvgm

echo "Verifying installation..."
which dvisvgm && dvisvgm --version || echo "dvisvgm not found in PATH"

echo ""
echo "If dvisvgm is still not found, try:"
echo "  export PATH=\"/Library/TeX/texbin:\$PATH\""
echo "  which dvisvgm"

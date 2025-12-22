#!/bin/bash
#
# Installation script for bentley_media_prep
# Deploys to /usr/local/bin for system-wide access
#

set -e

SCRIPT_NAME="bentley_media_prep.py"
INSTALL_NAME="bentley_media_prep"
INSTALL_DIR="/usr/local/bin"

echo "bentley_media_prep Installation"
echo "================================"
echo ""

# Check if script exists
if [ ! -f "$SCRIPT_NAME" ]; then
    echo "ERROR: $SCRIPT_NAME not found in current directory"
    exit 1
fi

# Check Python dependencies
echo "Checking Python dependencies..."
python3 -c "import mutagen" 2>/dev/null || {
    echo "ERROR: mutagen not installed"
    echo "Please run: pip install mutagen"
    exit 1
}

python3 -c "import PIL" 2>/dev/null || {
    echo "ERROR: Pillow not installed"
    echo "Please run: pip install Pillow"
    exit 1
}

echo "✓ Dependencies OK"
echo ""

# Install
echo "Installing to $INSTALL_DIR/$INSTALL_NAME"
echo "(This requires sudo access)"
echo ""

sudo cp "$SCRIPT_NAME" "$INSTALL_DIR/$INSTALL_NAME"
sudo chmod +x "$INSTALL_DIR/$INSTALL_NAME"

echo ""
echo "✓ Installation complete!"
echo ""
echo "You can now run: bentley_media_prep <directory> [jpeg_name]"
echo ""
echo "Examples:"
echo "  bentley_media_prep ~/Music/FLAC"
echo "  bentley_media_prep ~/Music/FLAC folder.jpg"

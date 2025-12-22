# bentley_media_prep

A command-line tool to extract and resize FLAC cover art to JPEG files.

## Overview

`bentley_media_prep` recursively processes directories containing FLAC files, extracting cover art from the first FLAC file in each folder and saving it as a resized 800x800 pixel JPEG.

## Features

- Recursively processes entire directory trees
- Extracts embedded cover art from FLAC metadata
- Resizes images to exactly 800x800 pixels (quality 95)
- Configurable output filename (defaults to cover.jpg)
- Verbose logging with timestamps
- Safe overwriting (creates backups not needed - use with care)

## Requirements

- Python 3.12.1 (or compatible)
- mutagen (FLAC metadata handling)
- Pillow (image processing)

## Installation

### 1. Install Python dependencies

```bash
pip install mutagen Pillow
```

### 2. Deploy to /usr/local/bin

```bash
cd ~/development/bentley_media_prep
sudo cp bentley_media_prep.py /usr/local/bin/bentley_media_prep
sudo chmod +x /usr/local/bin/bentley_media_prep
```

Or use the provided install script:

```bash
cd ~/development/bentley_media_prep
./install.sh
```

## Usage

### Basic usage (creates cover.jpg in each folder)
```bash
bentley_media_prep /path/to/music/directory
```

### Specify custom JPEG filename
```bash
bentley_media_prep /path/to/music/directory folder.jpg
```

### Examples
```bash
# Process entire music library
bentley_media_prep ~/Music/FLAC

# Create album_art.jpg instead of cover.jpg
bentley_media_prep ~/Music/FLAC album_art.jpg

# Process a specific artist directory
bentley_media_prep ~/Music/FLAC/Pink\ Floyd
```

## How It Works

1. Recursively walks through the specified directory
2. For each folder containing FLAC files:
   - Opens the first FLAC file found
   - Extracts the embedded cover art (front cover)
   - Resizes to exactly 800x800 pixels (stretches if needed)
   - Saves as JPEG with quality 95
   - Overwrites existing file with same name if present
3. Logs all operations with timestamps

## Error Handling

- **No FLAC files in folder**: Skipped silently
- **FLAC missing cover art**: Warning logged, continues processing
- **Permission issues**: Error logged, continues with next folder
- **Invalid directory**: Exits with error message

## Notes

- Only processes the first FLAC file in each folder (assumes one album per folder)
- Images are stretched to 800x800 if aspect ratio differs
- Existing JPEG files with the same name are overwritten
- FLAC files are never modified (read-only extraction)
- Hidden directories (starting with .) are skipped

## Platform Support

- macOS (zsh)
- Linux (bash)

## License

Proprietary - Leon's personal tooling

## Author

Leon (AWS EMEA Startups):

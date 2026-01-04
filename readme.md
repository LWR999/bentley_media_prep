# bentley_media_prep

A command-line tool to extract and resize FLAC cover art to JPEG files.

## Overview

`bentley_media_prep` recursively processes directories containing FLAC files, extracting cover art from the first FLAC file in each folder and saving it as a resized high-quality JPEG.

**Special Features:**
- **Personal Compilation Support**: Folders starting with "_" are treated as custom playlists/compilations
  - Strips "_" prefix to create album name
  - Updates metadata: ALBUM, ALBUMARTIST=Various Artists, COMPILATION=1
  - Preserves track-level artist names
  - Only creates cover art if it doesn't exist
- **Smart Cover Art Processing**: 
  - Regular albums: Always extracts/overwrites cover art
  - Maintains aspect ratio (longest side max 800px)
  - Never upscales images
  - JPEG quality 95

## Features

- Recursively processes entire directory trees
- Extracts embedded cover art from FLAC metadata
- **Personal compilation support** (folders starting with "_")
  - Normalizes album metadata across all tracks
  - Sets ALBUMARTIST to "Various Artists"
  - Sets compilation flag
  - Only creates cover art if missing
- **Smart resizing** maintains aspect ratio (longest side max 800px)
- **No upscaling** - preserves quality of smaller images
- Configurable output filename (defaults to cover.jpg)
- Verbose logging with timestamps
- Different behavior for compilations vs regular albums
- Regular albums: Always overwrites cover art
- Compilations: Preserves existing cover art

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

# Process personal compilations
# Folder "_Road Trip 2024" becomes album "Road Trip 2024" by Various Artists
bentley_media_prep ~/Music/Playlists
```

## How It Works

1. Recursively walks through the specified directory
2. For each folder containing FLAC files:
   
   **If folder starts with "_" (Personal Compilation):**
   - Strips "_" from folder name to get album name
   - Updates metadata for ALL tracks:
     - ALBUM = cleaned folder name
     - ALBUMARTIST = "Various Artists"
     - COMPILATION = 1
     - ARTIST preserved per track
   - Checks if cover art file already exists
   - If exists: skips (preserves existing)
   - If missing: extracts from first FLAC, resizes, saves
   
   **If regular folder (no "_"):**
   - No metadata changes
   - Extracts cover art from first FLAC
   - Resizes maintaining aspect ratio (longest side max 800px, no upscaling)
   - Saves as JPEG quality 95
   - Overwrites existing file if present

3. Logs all operations with timestamps and statistics

## Error Handling

- **No FLAC files in folder**: Skipped silently
- **FLAC missing cover art**: Warning logged, continues processing
- **Permission issues**: Error logged, continues with next folder
- **Invalid directory**: Exits with error message

## Notes

- **Personal compilations** (folders starting with "_"):
  - Metadata updated for ALL tracks in folder
  - Cover art only created if missing (non-destructive)
  - Great for custom playlists, road trip mixes, workout compilations
- **Regular albums**:
  - Metadata never modified
  - Cover art always extracted/overwritten
- Only processes the first FLAC file in each folder for cover art extraction
- Images maintain aspect ratio (no stretching)
- Never upscales (preserves quality of smaller images)
- FLAC files are never modified during cover art extraction (read-only)
- Hidden directories (starting with .) are skipped
- Regular albums: JPEG files overwritten (destructive for cover art)
- Compilations: Existing JPEG files preserved

## Platform Support

- macOS (zsh)
- Linux (bash)

## License

Proprietary - Leon's personal tooling

## Author

Leon (AWS EMEA Startups)

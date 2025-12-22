#!/usr/bin/env python3
"""
bentley_media_prep - Extract and resize FLAC cover art to JPEG files

Recursively processes directories containing FLAC files, extracting cover art
from the first FLAC in each folder and saving as resized JPEG.
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
from io import BytesIO

try:
    from mutagen.flac import FLAC
    from PIL import Image
except ImportError as e:
    print(f"ERROR: Missing required library: {e}")
    print("Please install required packages:")
    print("  pip install mutagen Pillow")
    sys.exit(1)


def log(message):
    """Log message with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def extract_cover_art(flac_path):
    """
    Extract cover art from FLAC file
    
    Args:
        flac_path: Path to FLAC file
        
    Returns:
        PIL Image object or None if no cover art found
    """
    try:
        audio = FLAC(flac_path)
        
        if not audio.pictures:
            return None
            
        # Get the first picture (usually front cover)
        picture = audio.pictures[0]
        image = Image.open(BytesIO(picture.data))
        return image
        
    except Exception as e:
        log(f"ERROR: Failed to extract cover art from {flac_path}: {e}")
        return None


def resize_and_save(image, output_path, size=(800, 800), quality=95):
    """
    Resize image to specified size and save as JPEG
    
    Args:
        image: PIL Image object
        output_path: Path to save JPEG
        size: Target size tuple (width, height)
        quality: JPEG quality (1-95)
    """
    try:
        # Convert to RGB if necessary (JPEG doesn't support transparency)
        if image.mode in ('RGBA', 'LA', 'P'):
            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
            if image.mode == 'P':
                image = image.convert('RGBA')
            rgb_image.paste(image, mask=image.split()[-1] if image.mode in ('RGBA', 'LA') else None)
            image = rgb_image
        elif image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Resize to exact dimensions (stretch if needed)
        resized = image.resize(size, Image.Resampling.LANCZOS)
        
        # Save as JPEG
        resized.save(output_path, 'JPEG', quality=quality, optimize=True)
        log(f"SUCCESS: Created {output_path}")
        
    except Exception as e:
        log(f"ERROR: Failed to save image to {output_path}: {e}")


def process_directory(root_dir, jpeg_name):
    """
    Recursively process directory tree, extracting cover art from FLAC files
    
    Args:
        root_dir: Root directory to process
        jpeg_name: Output JPEG filename
    """
    root_path = Path(root_dir).resolve()
    
    if not root_path.exists():
        log(f"ERROR: Directory does not exist: {root_dir}")
        sys.exit(1)
        
    if not root_path.is_dir():
        log(f"ERROR: Path is not a directory: {root_dir}")
        sys.exit(1)
    
    log(f"Starting processing of: {root_path}")
    log(f"Output filename: {jpeg_name}")
    log(f"Target size: 800x800, Quality: 95")
    log("-" * 80)
    
    folders_processed = 0
    folders_with_flac = 0
    images_created = 0
    
    # Walk the directory tree
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        # Find FLAC files in current directory
        flac_files = [f for f in filenames if f.lower().endswith('.flac')]
        
        if not flac_files:
            continue
            
        folders_with_flac += 1
        current_dir = Path(dirpath)
        log(f"Processing folder: {current_dir}")
        log(f"  Found {len(flac_files)} FLAC file(s)")
        
        # Process only the first FLAC file
        first_flac = current_dir / flac_files[0]
        log(f"  Extracting from: {first_flac.name}")
        
        # Extract cover art
        image = extract_cover_art(first_flac)
        
        if image is None:
            log(f"  WARNING: No cover art found in {first_flac.name}")
            continue
        
        original_size = image.size
        log(f"  Original cover art size: {original_size[0]}x{original_size[1]}")
        
        # Save resized image
        output_path = current_dir / jpeg_name
        resize_and_save(image, output_path)
        images_created += 1
        folders_processed += 1
        log("")
    
    # Summary
    log("-" * 80)
    log("Processing complete!")
    log(f"Folders scanned: {folders_with_flac}")
    log(f"Folders processed: {folders_processed}")
    log(f"Images created: {images_created}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Extract and resize FLAC cover art to JPEG files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  bentley_media_prep /path/to/music
  bentley_media_prep /path/to/music album_art.jpg
  bentley_media_prep ~/Music/FLAC folder.jpg
        """
    )
    
    parser.add_argument(
        'directory',
        help='Root directory to process (will recurse through all subdirectories)'
    )
    
    parser.add_argument(
        'jpeg_name',
        nargs='?',
        default='cover.jpg',
        help='Output JPEG filename (default: cover.jpg)'
    )
    
    args = parser.parse_args()
    
    try:
        process_directory(args.directory, args.jpeg_name)
    except KeyboardInterrupt:
        log("\nINTERRUPTED: Processing cancelled by user")
        sys.exit(130)
    except Exception as e:
        log(f"FATAL ERROR: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

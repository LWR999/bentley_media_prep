# bentley_media_prep - Setup and Testing Instructions

## What's Been Created

Your tool is ready in `~/development/bentley_media_prep/`:

```
bentley_media_prep/
├── .git/                    # Git repository initialized
├── .gitignore               # Python/IDE exclusions
├── README.md                # Full documentation
├── bentley_media_prep.py    # Main executable script
├── install.sh               # Installation helper
└── SETUP.md                 # This file
```

## Step 1: Install Python Dependencies

On your Mac, run:

```bash
pip install mutagen Pillow
```

Or if you prefer pip3:

```bash
pip3 install mutagen Pillow
```

## Step 2: Configure Git (First Time Only)

```bash
cd ~/development/bentley_media_prep
git config user.name "Leon"
git config user.email "your.email@example.com"
git add .
git commit -m "Initial commit: bentley_media_prep v1.0"
```

## Step 3: Test the Tool (Before Installing)

Run directly from development directory:

```bash
cd ~/development/bentley_media_prep
./bentley_media_prep.py --help
```

Test on a sample directory:

```bash
./bentley_media_prep.py /path/to/test/music/folder
```

## Step 4: Install to /usr/local/bin

Once testing is successful:

```bash
cd ~/development/bentley_media_prep
./install.sh
```

Or manually:

```bash
sudo cp bentley_media_prep.py /usr/local/bin/bentley_media_prep
sudo chmod +x /usr/local/bin/bentley_media_prep
```

## Step 5: Test System-Wide Installation

```bash
bentley_media_prep --help
bentley_media_prep ~/Music/some_test_folder
```

## Step 6: Push to GitHub

Create a new repo on GitHub, then:

```bash
cd ~/development/bentley_media_prep
git remote add origin git@github.com:yourusername/bentley_media_prep.git
git branch -M main
git push -u origin main
```

## Quick Test Command

To verify everything works without processing real files:

```bash
# Show help
./bentley_media_prep.py --help

# Test on empty directory (will do nothing but verify the tool runs)
mkdir -p /tmp/test_empty
./bentley_media_prep.py /tmp/test_empty
```

## Tool Usage

```bash
# Basic usage (creates cover.jpg)
bentley_media_prep /path/to/music

# Custom filename
bentley_media_prep /path/to/music folder.jpg

# Process specific folder
bentley_media_prep ~/Music/FLAC/Pink\ Floyd
```

## What It Does

1. Walks through all subdirectories recursively
2. For each folder with FLAC files:
   - Extracts cover art from the first FLAC
   - Resizes to 800x800 pixels (stretch to fit)
   - Saves as JPEG quality 95
3. Logs everything with timestamps

## Editing the Script

Use vi as preferred:

```bash
cd ~/development/bentley_media_prep
vi bentley_media_prep.py
```

After changes, reinstall:

```bash
./install.sh
```

## Troubleshooting

**Import errors:**
- Ensure mutagen and Pillow are installed for your Python 3.12.1

**Permission errors during install:**
- Make sure you have sudo access
- `/usr/local/bin` should be in your PATH

**Script not found after install:**
- Check: `which bentley_media_prep`
- Verify PATH includes `/usr/local/bin`

**Git commit fails:**
- Configure git user name and email first (see Step 2)

## Notes

- The tool is DESTRUCTIVE for JPEG files (overwrites existing)
- FLAC files are never modified (read-only)
- Uses verbose logging - you'll see everything it does
- Skips hidden directories (those starting with .)

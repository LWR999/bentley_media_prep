# bentley_media_prep v2.0 - Changelog

## Major Updates

### Personal Compilation Support
**Folders starting with "_" are now treated as personal compilations:**

- Strips the "_" from folder name to create album name
- Updates metadata for ALL FLAC files in the folder:
  - `ALBUM` = cleaned folder name (e.g., "_Road Trip 2024" → "Road Trip 2024")
  - `ALBUMARTIST` = "Various Artists"
  - `COMPILATION` = "1"
  - Track-level `ARTIST` remains unchanged
- Cover art: Only created if it doesn't already exist (non-destructive)

**Example:**
```
Folder: "_Summer Vibes 2024"
Result: 
  - Album name: "Summer Vibes 2024"
  - Album artist: "Various Artists"
  - Compilation flag set
  - Each track keeps its original artist
```

### Updated Cover Art Processing

**New Resize Behavior:**
- Maintains aspect ratio (no more stretching)
- Scales longest side to max 800px
- Never upscales (preserves smaller images)
- Quality remains at 95

**Examples:**
- 1200x1200 → 800x800
- 1500x1000 → 800x533
- 1000x1500 → 533x800
- 600x600 → 600x600 (no upscale)

**Processing Rules by Folder Type:**

| Folder Type | Metadata Updates | Cover Art Behavior |
|-------------|------------------|-------------------|
| Personal Compilation (_prefix) | YES (all tracks) | Only if missing |
| Regular Album | NO | Always (overwrites) |

### Enhanced Reporting

**New statistics tracked:**
- Personal compilations processed (metadata updates)
- Personal compilations skipped (cover art exists)
- Regular albums processed
- Images created (new files)
- Images overwritten (replaced existing)

**Sample output:**
```
Processing complete!
Folders with FLAC files: 250
Personal compilations processed: 15
Personal compilations skipped (cover art exists): 5
Regular albums processed: 230
Images created (new): 235
Images overwritten (existing): 230
```

## Use Cases

### Converting iTunes/Spotify Playlists
1. Export playlist to folder with "_" prefix
2. Run bentley_media_prep
3. Result: Unified album in Bentley with proper metadata

### Re-running on Existing Library
- Regular albums: Cover art refreshed/updated
- Personal compilations: Metadata preserved if cover art exists
- Efficient for incremental updates

## Migration Notes

**From v1.0:**
- Old behavior: Stretched images to 800x800
- New behavior: Maintains aspect ratio
- Run on existing library to update aspect ratios

**Recommendation:**
Test on a small subset first, especially if you have custom-edited cover art files you want to preserve.

## Version History

**v2.0 (January 2026)**
- Added personal compilation support (_prefix folders)
- Changed resize to maintain aspect ratio
- Added no-upscaling logic
- Enhanced reporting with detailed statistics
- Different behavior for compilations vs regular albums

**v1.0 (December 2024)**
- Initial release
- Basic cover art extraction
- 800x800 stretch resize
- Skip existing cover art

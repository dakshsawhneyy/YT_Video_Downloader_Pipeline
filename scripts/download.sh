#!/bin/bash

# read -p "Enter video URL: " url
# yt-dlp -o "../downloads/%(title)s.%(ext)s" "$url"

DOWNLOAD_DIR="downloads"

# Sorting files based on extension
for file in "$DOWNLOAD_DIR"/*; do
    if [[ -f "$file" ]]; then
        ext="${file##*.}"

        # Add date folder inside extention for proper record
        TODAY=$(date +"%d-%m-%Y")
        mkdir -p "$DOWNLOAD_DIR/$ext/$TODAY"    # Create Date Folder

        mv "$file" "$DOWNLOAD_DIR/$ext/$TODAY/" 2>/dev/null     # Move the file
    fi
done

echo "Files sorted by extension into directories."
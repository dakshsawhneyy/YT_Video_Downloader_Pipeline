from yt_dlp import YoutubeDL
import os
import json
from datetime import timedelta
import argparse
# from download import download_video

# Creating CLI Arguments
def parse_args_extract():
    parser = argparse.ArgumentParser(description="Extract video metadata from a URL using yt-dlp.")
    
    parser.add_argument(
        '--save',
        action="store_true",
        help="Save metadata to video_metadata.json"
    )
    
    parser.add_argument(
        '--download',
        action="store_true",
        help="Download the video after extracting metadata"
    )
    
    parser.add_argument(
        '--url',
        required=False,
        type=str,
        help="URL of the video to extract metadata from (optional, if not provided will use input prompt)"
    )
    
    parser.add_argument(
        '--add-to-db',
        action="store_true",
        help="Add metadata to SQLite database"
    )
    
    # Adding --cli tag for running inside docker
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run in CLI mode (for Docker compatibility)"
    )
    
    # Adding GUI Tag as well
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Run in GUI mode"
    )
    
    return parser.parse_args()


# Creating function for reusing in another file
def ydl_instance_creation(url):
    # dictionary called ydl_opts that holds options for the YoutubeDL object
    yds_opts = {
        'quiet': True,  # suppresses most console output to keep things clean
        'skip_download': True, # tells it not to download the actual video, just fetch info.
        'dump_single_json': True # tells it to retrieve and output all the video metadata as JSON.
    }

    # Creates a YoutubeDL instance using the options ydl_opts
    with YoutubeDL(yds_opts) as ydl:
        # try-catch for invalid url's
        try:
            info = ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"Error: {e}")
            exit(1)

    print("\n")
    print("Title: ", info.get('title'))

    # Show Duration in HH:MM:SS
    duration = str(timedelta(seconds=info.get('duration')))
    print("Duration:", duration)

    print("Format: ", info.get('ext'))
    print("Tags:", info.get('tags'))
    
    return info


#! Store these info into video_metadata.json
def save_summary(info, args):
    # Need to create own object what we need to store to metadata_file
    metadata = {
        "Title": info.get("title"),
        "Duration": str(timedelta(seconds=info.get('duration'))),
        "Format": info.get("ext"),
    }

    # Check if video_metadata.json is present or not, if not create it
    if args.save:
        metadata_file = "video_metadata.json"
        if not os.path.exists(metadata_file):
            with open(metadata_file, "w") as f:
                json.dump([], f, indent=4)

        # Check if it is not empty
        with open(metadata_file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

        # Append only works on lists
        data.append(metadata)

        # Now push the data into metadata_file
        with open(metadata_file, "w") as f:
            json.dump(data, f, indent=4)
        print("✅ Metadata saved to video_metadata.json")
    

if __name__ == "__main__":
    args = parse_args_extract()
    url = args.url or input("Enter Url: ")
    info = ydl_instance_creation(url)   # fetching info from this function
    save_summary(info, args)    
    
    if args.download:
        download_video(url)
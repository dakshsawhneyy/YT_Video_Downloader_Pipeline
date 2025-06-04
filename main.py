from yt_dlp import YoutubeDL
import os
from datetime import timedelta
import argparse
import sys

# Extract.py
from metadata.extract import parse_args_extract # arg_parse fxn
from metadata.extract import ydl_instance_creation  # extract info
from metadata.extract import save_summary # to save summary inside json

# DB
from metadata.db_setup import db_setup # Table setup
from metadata.insert_to_db import insert_db # Insert into DB
from metadata.fetch_metadata_db import fetch_db # fetch data from db

# cli_interface
from metadata.cli_interface import arg_parser_cli
from metadata.cli_interface import list_videos
from metadata.cli_interface import search_by_title
from metadata.cli_interface import search_by_filter

# download
from metadata.download import download_video

# delete
from metadata.delete_from_db import find_entries_by_keyword
from metadata.delete_from_db import delete_db

# GUI
from Gui.gui_interface import start_gui

if __name__ == "__main__":    
    
    # GUI
    if "--gui" in sys.argv:
        start_gui()
        exit()
    
    # Need to give condition for passing two parse_args fxns
    if any(arg in ["--list", "--filter", "--search", "--delete"] for arg in sys.argv):
        args_cli = arg_parser_cli()     # Passing cli_interface one
        if args_cli.list:
            list_videos()
        elif args_cli.search:
            search_by_title(args_cli.search)
        elif args_cli.filter:
            search_by_filter(args_cli.filter)
        elif args_cli.delete:
            # Condition if delete comes, none other will come
            matches = find_entries_by_keyword(args_cli.delete)
            if not matches:
                print("❌ No entries found with that keyword.")
            else:
                print("Found entries:")
                for match in matches:
                    print(f"ID: {match[0]}, Title: {match[1]}, Duration: {match[2]}")
                confirm = input(f"Are you sure want to delete these {len(matches)} entries? (y/n): ")
                if confirm.lower() in ('y', 'yes'):
                    deleted = delete_db([row[0] for row in matches])
                    print(f"✅ Deleted {deleted} entries.")
                else:
                    print("❎ Deletion cancelled.")
        else:
            print("❌ No valid option provided. Use --help for available commands.")
    else:
        args = parse_args_extract()
        url = args.url or input("Enter Url: ")
        info = ydl_instance_creation(url)
        if not info:
            print("❌ Failed to extract video info.")
            exit(1)
            
        duration = str(timedelta(seconds=info.get("duration")))
        
        save_summary(info, args)

        print("\n")
        
        db_setup()
        if args.add_to_db:
            insert_db(info, duration)
        fetch_db()
        
        print("\n")
        
        if args.download:
            download_video(url)
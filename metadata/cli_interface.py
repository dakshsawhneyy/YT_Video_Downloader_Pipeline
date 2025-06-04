import argparse
import sqlite3

def list_videos():
    conn = sqlite3.connect('videos.db')    # connect
    cursor = conn.cursor() # 
    cursor.execute("SELECT * FROM videos_metadata")
    rows = cursor.fetchall()
    print("-" * 30)
    for row in rows:
        id, title, duration, format = row
        print(f"ID: {id} | Title: {title} | Duration: {duration} | Format: {format}")
    print("-" * 30)
    conn.close()
    
def search_by_title(keyword):
    conn = sqlite3.connect('videos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos_metadata WHERE LOWER(title) LIKE ?", ('%' + keyword.lower() + '%',)) # A tuple with one string element -- % mtlb agey piche koi char mix up ho skta hai 
    rows = cursor.fetchall()
    print("-" * 30)
    if rows:
        for row in rows:
            id, title, duration, format = row
            print(f"ID: {id} | Title: {title} | Duration: {duration} | Format: {format}")
    else:
        print("❌ No videos found with that title.")
    print("-" * 30)
    conn.close()
    
    return rows  # 

def search_by_filter(keyword):
    conn = sqlite3.connect('videos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos_metadata WHERE format = ?", (keyword,)) # not percentage, agey piche koi aur char nhi ho skta exact el chaiye
    rows = cursor.fetchall()
    print("-" * 30)
    if rows: 
        for row in rows:
            id, title, duration, format = row
            print(f"ID: {id} | Title: {title} | Duration: {duration} | Format: {format}")
    else:
        print("❌ No videos found with that title.")
    print("-" * 30)
    conn.close()

def arg_parser_cli():
    parser = argparse.ArgumentParser(description="CLI to manage video metadata in SQLite database.")
    
    parser.add_argument('--list', action='store_true', help="List all videos in the database")
    parser.add_argument('--search', action='store', type=str, help="Search for a video by title")
    parser.add_argument('--filter', type=str, help="Filter videos by format (e.g., mp4, mkv)")
    parser.add_argument(
        '--delete',
        type=str,
        help=("Delete metadata from SQLite database by ID, ")
    )
    
    return parser.parse_args()


if __name__ == "__main__":
    args = arg_parser_cli()

    if args.list:
        list_videos()
    elif args.search:
        search_by_title(args.search)
    elif args.filter:
        search_by_filter(args.filter)
    else:
        print("❌ No valid option provided. Use --help for available commands.")
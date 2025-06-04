from yt_dlp import YoutubeDL
import sqlite3
from datetime import timedelta


def insert_db(info, duration):
    # Connect to sqlite
    conn = sqlite3.connect('videos.db')
    cursor = conn.cursor()

    # Insert into table
    cursor.execute('''
        INSERT INTO videos_metadata (title, duration, format, url)
        VALUES (?, ?, ?, ?)    
    ''', (info.get('title'), duration, info.get('ext'), info.get('webpage_url'))
    )

    # Save and close
    conn.commit()
    conn.close()

    print("✅ Metadata inserted into SQLite database. \n")
    
if __name__ == "__main__":
    url = input("Enter url: ")
    
    # Create options for yt_dlp
    yts_ops = {
        'quiet': True,
        'skip_download': True,
        'dump_single_json': True
    }

    # Create instance with help of these options
    with YoutubeDL(yts_ops) as ydl:
        # Verify if url is correct or not
        try:
            info = ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"Error: {e}")
            exit(1)

    duration = str(timedelta(seconds=info.get("duration")))
    
    insert_db(info, duration)
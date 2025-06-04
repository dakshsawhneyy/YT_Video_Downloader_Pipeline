from yt_dlp import YoutubeDL
import sqlite3

import utils.logger as logger

def find_entries_by_keyword(keyword):
    try:
        conn = sqlite3.connect("videos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM videos_metadata WHERE LOWER(title) LIKE ?", ('%' + keyword.lower() + '%',))
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        return []
    finally:
        conn.close()

def delete_db(ids):
    try:
        conn = sqlite3.connect('videos.db')
        cursor = conn.cursor()
        cursor.executemany('DELETE FROM videos_metadata WHERE id = ?', [(i,) for i in ids])
        conn.commit()
        deleted_count = cursor.rowcount
        return deleted_count
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        return 0
    finally:
        conn.close()
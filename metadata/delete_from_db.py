from yt_dlp import YoutubeDL
import sqlite3


def find_entries_by_keyword(keyword):
    conn = sqlite3.connect("videos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos_metadata WHERE LOWER(title) LIKE ?", ('%' + keyword.lower() + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def delete_db(ids):
    conn = sqlite3.connect('videos.db')
    cursor = conn.cursor()
    cursor.executemany('DELETE FROM videos_metadata WHERE id = ?', [(i,) for i in ids])
    conn.commit()
    deleted_count = cursor.rowcount
    conn.close()
    return deleted_count
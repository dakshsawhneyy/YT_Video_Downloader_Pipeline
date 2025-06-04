import sqlite3
from utils.logger import logger

def fetch_db():
    # Connect to db
    conn = sqlite3.connect('videos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM videos_metadata')
    rows = cursor.fetchall()    # Return tuple as output

    # print(rows) # It is a list of tuples

    print("Printing all videos metadata from the database: \n")
    print("-" * 30)
    for row in rows:
        id, title, duration, format, url = row  # assigning values of tuple
        print(f"ID: {id}")
        print(f"Title: {title}")
        print(f"Duration: {duration}")
        print(f"Format: {format}")
        # print(f"URL: {url}")
        print("-" * 30)
            
    # Close the Database
    conn.close()
    
    return rows

if __name__ == "__main__":
    fetch_db()
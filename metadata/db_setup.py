import sqlite3
from utils.logger import logger

def db_setup():
    # opens or creates the DB file - Connect to database (creates file if not exists)
    conn = sqlite3.connect('videos.db')

    # Create a cursor to execute SQL commands
    cursor = conn.cursor()

    # sends SQL commands to create the table - Create table if it does not exist already
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            duration TEXT,
            format TEXT,
            url TEXT
        )
    ''')

    logger.info("🔵 Table 'videos_metadata' created or already exists.🟣")
    print("🔵 Table 'videos_metadata' created or already exists.🟣 \n")

    conn.commit() # saves changes.
    conn.close() # closes connection safely.
    
if __name__ == "__main__":  
    db_setup()
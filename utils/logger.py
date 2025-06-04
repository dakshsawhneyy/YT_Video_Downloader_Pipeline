# for profession grade logging, log rotations and much more
from loguru import logger
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# # os.path.basename(__file__) → Extracts just the file name from the path:||| os.path.splitext(...)[0] → Removes the extension (.py) and returns only the base name:
# FILE_NAME = os.path.splitext(os.path.basename(__file__))[0] # __file__ → Gives the full path of the current script

logger.add(
    os.path.join(LOG_DIR, f"app.log"),
    rotation="10 MB",  # Rotate log file when it reaches 10 MB
    retention="7 days",  # Keep logs for 7 days
    level="INFO",  # Log level
    compression="zip",  # Compress rotated logs
    enqueue=True,
    format="{time} {level} {message}",  # Log format
)

logger.info("Logger initialized successfully.")
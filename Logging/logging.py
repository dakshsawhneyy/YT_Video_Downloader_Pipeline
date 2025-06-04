import logging
import os 
from datetime import datetime

# Create log directory if not exists
os.makedirs("Logging/logs", exist_ok=True)

# Log filename with date
log_filename = datetime.now().strftime("Logging/logs/log_%d-%m-%Y.log")

# Setting up the logging configuration (for the whole file/app):
logging.basicConfig(
    filename=log_filename,  # Save logs in a file
    level=logging.INFO, # Only log info and above (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s' # Format of the log messages
)

def get_logger():
    return logging.getLogger(__name__)
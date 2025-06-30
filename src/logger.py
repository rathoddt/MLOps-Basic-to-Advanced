import logging
import os
from datetime import datetime

LOGS_DIR="logs"
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")
# LOG_FORMAT = '%(asctime)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s'
# file + function + line number
LOG_FORMAT = '%(asctime)s - %(module)s.%(funcName)s:%(lineno)d - %(levelname)s - %(message)s'
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
console_handler.setLevel(logging.INFO)

def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger
import logging
import os
from datetime import datetime

# ---------------------------------------------------------
# FIX: Get project root directory instead of current folder
# ---------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))   # <-- MLPRJECT/
LOG_FOLDER = os.path.join(ROOT_DIR, "logs")
os.makedirs(LOG_FOLDER, exist_ok=True)

# Create log file inside project root's logs folder
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

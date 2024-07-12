import logging
import os
from datetime import datetime

LOG_DIR = "pylogs"
LOG_DIR_PATH = os.path.join(os.getcwd(),LOG_DIR)

#create log directory usinng os.makedirs
os.makedirs(LOG_DIR, exist_ok=True)

#create log filename
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d %H:%M%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}"
log_file_path = os.path.join(LOG_DIR, file_name)

#configure
logging.basicConfig(level=logging.INFO, filename=log_file_path, format="%(asctime)s %(levelname)s %(module)s ========>%(message)s",
                    datefmt="%d-%m-%Y %H:%M")

#create oject for logging
logger = logging.getLogger()

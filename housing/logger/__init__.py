import logging
from datetime import datetime
import os

log_dir = "housing_logs"

now = datetime.now()

current_time_stamp = f"{now.strftime('%Y-%m-%d_%H:%M-%S')}"

log_file_name = f"log_{current_time_stamp}.log"

os.makedirs(log_dir, exist_ok = True)

log_file_path = os.path.join(log_dir, log_file_name)

logging.basicConfig(filename = log_file_path,
                    filemode="w",
                    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)
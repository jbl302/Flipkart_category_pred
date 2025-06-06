import logging
import os
from datetime import datetime

"""
creating log files adding date, time , message
name of file will be timestamp
"""

Log_file = f"{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.log"

log_path = os.path.join(os.getcwd(),"logs",Log_file)

os.makedirs(log_path,exist_ok=True) # exist then append in it

Log_file_path = os.path.join(log_path,Log_file)

logging.basicConfig(
 filename=Log_file_path,
 format="%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
 level=logging.INFO,
)

if __name__ == "__main__":
  logging.info("logging has started")
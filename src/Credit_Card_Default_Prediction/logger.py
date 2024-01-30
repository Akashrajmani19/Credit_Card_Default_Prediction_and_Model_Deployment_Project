import logging
import os
from datetime import datetime

# Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Log file path
log_path = os.path.join(os.getcwd(),'logs')
# Creation of directory
os.makedirs(log_path,exist_ok = True) # if already exist then it will not create a new file else it will create
# now join the path and file name
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# LOgging configuration
logging.basicConfig(level = logging.INFO,
                    filename = LOG_FILE_PATH,
                    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )

if __name__ =="__main__":
    logging.info('testing')
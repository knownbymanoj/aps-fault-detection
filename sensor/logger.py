import logging
import os
from datetime import datetime
import os

#log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#create folder if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

'''
format: This specifies the format of the log output. 
The format string uses placeholders to define the structure of each log message. 

In this case, the placeholders are: 
%(asctime)s: The time at which the log message was created, in a formatted string.
%(lineno)d: The line number where the logging call was made. 
%(name)s: The name of the logger used to log the message. 
%(levelname)s: The logging level of the message (e.g. INFO, WARNING, ERROR, etc.). 
%(message)s: The log message itself. 

level: This specifies the minimum severity level of the messages to be logged. 
In this case, only messages with a severity level of INFO or higher will be logged.
'''
# Matthew Tong Lab 9
import logging
import logging.handlers
from datetime import datetime

# stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# Configure Logging
logging.basicConfig(
    filename = 'sample.log',
    format = '%(asctime)s | %(levelname)s | %(filename)s | %(message)s',
    level = logging.INFO
)

# Console Logging
console = logging.StreamHandler()
console.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.exception('exp')




# Matthew Tong Lab 9
import logging
import logging.handlers

# Logging Configuration
logging.basicConfig(
    filename = 'my_sample_app.log',
    level = logging.INFO,
    format = '%(asctime)s - %(message)',
    datefmt = '%H:%M:%S'
)

debugLog = logging.getLogger("SystemConfiguredLogger")

debugLog.log(logging.CRITICAL, "PC WILL BLOW UP")

debugLog.critical("There is no more disk space")
debugLog.error("File Not Found")
debugLog.warning("Low System Memory")
debugLog.info("Failed Attempted Login")

# Logging to Config File
logger = logging.getLogger()


logger.addHandler(
    logging.handlers.TimedRotatingFileHandler(
        filename = "archived_log.log",
        when = "D",
        backupCount = 3
    )
)

# Logging to Console






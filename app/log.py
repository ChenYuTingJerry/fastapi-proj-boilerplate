import logging

LOG_PATH = './app.log'
LOG_SIZE = 2048
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '[%(asctime)s.%(msecs)03dZ] [%(levelname)s] %(message)s'

logger = logging.getLogger()

sh = logging.StreamHandler()
fh = logging.FileHandler(LOG_PATH)
formatter = logging.Formatter(LOG_FORMAT, datefmt='%Y-%m-%dT%H:%M:%S')
sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.setLevel(LOG_LEVEL)
logger.addHandler(sh)
logger.addHandler(fh)

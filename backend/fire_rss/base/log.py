import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s %(filename)s %(funcName)s() "
    "L%(lineno)d: %(message)s",
)
std_handler = logging.StreamHandler()
std_handler.setFormatter(formatter)

logger.addHandler(std_handler)

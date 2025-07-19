import logging

formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s %(filename)s %(funcName)s() L%(lineno)d: %(message)s",
)
std_handler = logging.StreamHandler()
std_handler.setFormatter(formatter)


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(std_handler)
    return logger


logger = get_logger()

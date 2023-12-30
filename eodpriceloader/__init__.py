import logging

loggers = logging.getLogger(__name__)
loggers.setLevel(logging.INFO)

logging.root.setLevel(logging.INFO)

logger_handler = logging.StreamHandler()
logger_handler.setLevel(logging.INFO)

logger_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s -- %(message)s')
logger_handler.setFormatter(logger_formatter)
loggers.addHandler(logger_handler)
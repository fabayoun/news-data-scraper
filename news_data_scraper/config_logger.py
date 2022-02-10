import logging

LOGGING_LEVEL = logging.INFO


def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(LOGGING_LEVEL)

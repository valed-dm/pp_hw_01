"""https://www.lesinskis.com/python-excepthook-logging.html"""

import sys

from .custom_logging import Logging

log = Logging("analyzer")
logger = log.get_logger()


def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
    """Handler for unhandled exceptions that will write to the logs"""
    if issubclass(exc_type, KeyboardInterrupt):
        # call the default excepthook saved at __excepthook__
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.critical("Unhandled exception caught", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_unhandled_exception

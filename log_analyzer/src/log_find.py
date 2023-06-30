"""Searches for input log file to be processed"""

import os
import sys

from .helpers.log_last_log import find_last_log
from .helpers.log_last_report import find_last_report
from .logging import Logging

logging = Logging("analyzer")
logger = logging.get_logger()


def find_log(log_dir, report_dir):
    """Returns last log file to be processed
    if no report for it has been created previously.
    """

    llog = find_last_log(log_dir)
    report = find_last_report(report_dir)

    if report.date < llog.date:
        return llog

    logger.info("report %s already exists", os.path.join(report_dir, report.name))
    sys.exit()

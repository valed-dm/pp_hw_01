"""Searches for input log file to be processed"""

import os

from .helpers.log_last_log import find_last_log
from .helpers.log_last_report import find_last_report


def find_log(log_dir, report_dir):
    """Returns last log file to be processed
    if no report for it has been created previously.
    """

    llog = find_last_log(log_dir)
    if isinstance(llog, str):
        return llog

    report = find_last_report(report_dir)
    if report.date < llog.date:
        return llog

    msg = f"report {os.path.join(report_dir, report.name)} already exists"
    return msg

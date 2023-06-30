"""Checks if a report has been already created and up-to-date"""

import os
import re
from datetime import datetime

from ..schemas import Report


def find_last_report(report_dir):
    """Returns up-to-date report if exists"""

    report = Report()
    try:
        with os.scandir(report_dir) as it:
            for entry in it:
                if re.fullmatch("report-*.*.*.html", entry.name):
                    r_date = datetime.strptime(
                        entry.name.lstrip("report-").rstrip(".html"),
                        '%Y.%m.%d'
                    ).date()
                    if r_date > report.date:
                        report.name = entry.name
                        report.date = r_date
        return report
    except FileNotFoundError:
        return report

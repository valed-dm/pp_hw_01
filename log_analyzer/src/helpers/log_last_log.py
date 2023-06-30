"""Input log file is checked if exists or valid and sorted by date"""

import os
import re
import sys
from datetime import datetime

from ..logging import Logging
from ..schemas import Log

logging = Logging("analyzer")
logger = logging.get_logger()


def find_last_log(log_dir):
    """Searches for log file to be processed"""

    llog = Log()  # llog -> latest_log
    try:
        with os.scandir(log_dir) as it:
            for entry in it:
                if re.fullmatch("nginx-access-ui.log-*(.*?)(log|gz)$", entry.name):
                    # log_date_ext = log date, log extension
                    log_date_ext = entry.name.lstrip("nginx-access-ui.log-").split(".")
                    log_date = datetime.strptime(log_date_ext[0], '%Y%m%d').date()
                    log_ext = log_date_ext[1]
                    if llog.date < log_date:
                        llog.name = entry.name
                        llog.ext = log_ext
                        llog.date = log_date
        if not llog.name:
            logger.error("log files (.log, .gz) are not found in %s directory", log_dir)
            sys.exit("log files not found")
        return llog
    except FileNotFoundError:
        logger.error("log source dir %s does not exist", log_dir)
        sys.exit()

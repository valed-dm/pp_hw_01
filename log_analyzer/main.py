"""
Log analyzer main file
https://mail.python.org/pipermail/python-list/2016-April/857869.html
"""
import sys

from src.helpers import create_arg_parser
from src.helpers import log_cfg
from src.helpers import log_path
from src.log_find import find_log
from src.log_parser import Parser
from src.log_report import log_report
from src.logging import Logging

# !/usr/bin/env python
# -*- coding: utf-8 -*-

logging = Logging("analyzer")
logger = logging.get_logger()

arg_parser = create_arg_parser()
args = arg_parser.parse_args()
config = log_cfg(path=args.config)


def main():
    """Log analyzer main"""

    log = find_log(
        log_dir=config.log_dir,
        report_dir=config.report_dir
    )
    if isinstance(log, str):
        logger.info(log)
        return
    log_src = log_path(config.log_dir, log.name)
    parser = Parser(
        file=log_src,
        ext=log.ext,
        report_size=int(config.report_size)
    )
    report_data = parser.log_processor()
    if isinstance(report_data, str):
        logger.info(report_data)
        return
    log_report(
        r_date=log.date,
        r_data=report_data,
        r_dir=config.report_dir,
    )


if __name__ == "__main__":
    sys.exit(main())

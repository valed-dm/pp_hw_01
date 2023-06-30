"""Parsed log data HTML report builder """

import os
from pathlib import Path

from .helpers import report_name
from .helpers import template
from .logging import Logging

logging = Logging("analyzer")
logger = logging.get_logger()


def log_report(r_date, r_data, r_dir):
    """HTML report creator"""

    result_rendered = template.render({"table_json": r_data})
    r_name = report_name(r_date)
    r_path = os.path.join(r_dir, r_name)
    if not os.path.isdir(r_dir):
        os.mkdir(r_dir)
    with Path(r_path).open('w', encoding="utf-8") as f:
        f.write(result_rendered)
        logger.info("report %s successfully created", r_path)

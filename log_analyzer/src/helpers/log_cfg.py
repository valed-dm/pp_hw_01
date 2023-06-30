"""Creates a log analyzer app configuration"""

import configparser
import re
import sys
from os.path import exists

from ..logging.custom_logging import Logging
from ..schemas import ConfigDefault

log = Logging("analyzer")
logger = log.get_logger()


def log_cfg(path):
    """Log analyzer app configuration creator"""

    config = ConfigDefault()

    if path:
        config_exists = exists(path)
        config_file_format_valid = re.fullmatch("(.*?)(ini|conf)$", path)

        if config_exists and config_file_format_valid:
            logger.info("app config file on path %s is used.", path)
            try:
                path = rf"{path}"
                cfg = configparser.ConfigParser()
                cfg.read(path)
                cfg = cfg["DEFAULT"]
                log_dir = cfg.get("LOG_DIR", None)
                report_dir = cfg.get("REPORT_DIR", None)
                report_size = cfg.get("REPORT_SIZE", None)
                config = ConfigDefault(
                    log_dir=log_dir if log_dir else config.log_dir,
                    report_dir=report_dir if report_dir else config.report_dir,
                    report_size=int(report_size) if report_size else config.report_size
                )
                return config

            except configparser.ParsingError as e:
                logger.error(e.message)
                sys.exit("config file parsing error")
        else:
            if not config_file_format_valid:
                logger.error(
                    "app config file on path %s is not valid."
                    " Default config values are used."
                    , path
                )
            else:
                logger.error(
                    "app config file on path %s does not exists."
                    " Default config values are used."
                    , path
                )

            return config

    logger.info("Path to config file is not provided. Default config values are used.")
    return config

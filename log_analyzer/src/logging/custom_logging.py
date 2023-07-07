"""logging.yaml -> https://gist.github.com/kingspp/9451566a5555fb022215ca2b7b802f19"""

import logging
import os
import sys
from logging import config as cfg
from logging import handlers
from pathlib import Path

import yaml

from .custom_rotating_file_handler import CustomRotatingFileHandler


class Logging:
    """logger creator class"""

    def __init__(self, logger_name, default_path="logging.yaml"):
        self.logger_name = logger_name
        self.default_path = default_path

    def get_logger(self):
        """logger creator"""

        if os.path.exists(self.default_path):
            handlers.RotatingFileHandler = CustomRotatingFileHandler
            with Path(self.default_path).open("rt", encoding="utf-8") as f:
                logging_config = yaml.safe_load(f.read())
                cfg.dictConfig(logging_config)
            logger = logging.getLogger(self.logger_name)
            return logger

        file_handler = logging.FileHandler(filename='tmp.log')
        stdout_handler = logging.StreamHandler(stream=sys.stdout)
        hlrs = [file_handler, stdout_handler]

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname).1s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=hlrs
        )

        root = logging.getLogger()
        root.error('Failed to load logger configuration file. Using default config.')
        return root

"""CustomRotatingFileHandler creates log dir"""

import os
from logging import handlers


class CustomRotatingFileHandler(handlers.RotatingFileHandler):
    """Log dir creator"""

    def __init__(
            self,
            filename,
            mode='a',
            maxBytes=0,
            backupCount=0,
            encoding=None,
            delay=False,
            errors=None
    ):
        # creates directory if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        super().__init__(filename, mode, maxBytes, backupCount, encoding, delay, errors)

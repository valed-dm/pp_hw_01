"""Source log path creator"""

import os


def log_path(log_dir, file_name):
    """Source log path creator"""

    source_path = os.path.join(log_dir, file_name)
    return source_path

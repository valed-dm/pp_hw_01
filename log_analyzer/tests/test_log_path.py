"""Testing ./helpers/log_path.py"""

import unittest

from ..src.helpers import log_path


class TestLogPath(unittest.TestCase):
    """Testing log file path creator"""

    def test_log_path(self):
        """Testing log path creation"""

        path = log_path(
            log_dir="./log",
            file_name="nginx-access-ui.log-20170630.log"
        )
        self.assertEqual(path, "./log/nginx-access-ui.log-20170630.log")


if __name__ == "__main__":
    unittest.main()

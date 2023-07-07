"""Full testing of an input log file searching"""

import unittest
from datetime import datetime

from ..src.helpers import find_last_log, find_last_report
from ..src.log_find import find_log


class TestFindLog(unittest.TestCase):
    """Testing log file input"""

    def test_find_log(self):
        """Testing if the latest log file is chosen"""

        llog = find_log(
            log_dir="./tests/t_log",
            report_dir=""
        )
        self.assertEqual(llog.name, "nginx-access-ui.log-20230623.log")
        self.assertEqual(llog.ext, "log")

    def test_log_dir_not_exists(self):
        """Testing log analyzer response if log source dir is not found"""

        log_dir = "./tests/t_log_1"
        msg = find_last_log(log_dir)
        self.assertEqual(msg, "log source dir ./tests/t_log_1 does not exist")

    def test_valid_log_files(self):
        """Testing if .log, .gz extensions filter works for input files"""

        log_dir = "./tests/t_log_2"
        msg = find_last_log(log_dir)
        self.assertEqual(msg, "log files (.log, .gz) are not found in ./tests/t_log_2 directory")

    def test_find_last_report(self):
        """Testing if the latest report file is found"""

        report = find_last_report(report_dir="./tests/t_reports")
        self.assertEqual(report.name, "report-2023.06.23.html")

    def test_return_report_default_values(self):
        """
        Testing report default date value which is used
        for last report search by passing a non-existing reports dir path.
        """

        report = find_last_report(report_dir="./tests/t_reports_1")
        self.assertEqual(report.name, "")
        self.assertEqual(report.date, datetime.strptime("19000101", '%Y%m%d').date())


if __name__ == "__main__":
    unittest.main()

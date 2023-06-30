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

        with self.assertLogs("analyzer") as captured:
            log_dir = "./tests/t_log_1"
            try:
                find_last_log(log_dir)
            except SystemExit:
                pass
            self.assertEqual(
                captured.records[0].getMessage(),
                f"log source dir {log_dir} does not exist"
            )

    def test_valid_log_files(self):
        """Testing if .log, .gz extensions filter works for input files"""

        with self.assertLogs("analyzer") as captured:
            log_dir = "./tests/t_log_2"
            try:
                find_last_log(log_dir)
            except SystemExit:
                pass
            self.assertEqual(
                captured.records[0].getMessage(),
                f"log files (.log, .gz) are not found in {log_dir} directory"
            )

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

"""Testing report creation"""

import os
import shutil
import unittest
from datetime import datetime
from os.path import exists
from pathlib import Path

from .t_reports.report_data import report_data
from ..src.log_report import log_report


class TestlogReport(unittest.TestCase):
    """Testing report file is created"""

    def setUp(self):
        """Test data"""

        self.work_dir = Path.cwd()
        self.report_dir = "tests/t_report"
        self.report_dir_abs_path = os.path.join(self.work_dir, self.report_dir)
        self.report_date = datetime.strptime("20230623", '%Y%m%d').date()

    def tearDown(self):
        """Delete t_report dir"""

        if exists(self.report_dir_abs_path):
            shutil.rmtree(self.report_dir_abs_path)

    def test_report_created(self):
        """Report creation test"""

        with self.assertLogs("analyzer") as captured:
            log_report(
                r_date=self.report_date,
                r_data=report_data,
                r_dir=self.report_dir
            )
            self.assertEqual(
                captured.records[0].getMessage(),
                "report tests/t_report/report-2023.06.23.html successfully created"
            )


if __name__ == "__main__":
    unittest.main()

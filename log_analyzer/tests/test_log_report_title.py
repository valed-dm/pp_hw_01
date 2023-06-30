"""Testing report title"""

import os
import shutil
import unittest
from datetime import datetime
from os.path import exists
from pathlib import Path

from bs4 import BeautifulSoup

from .t_reports.report_data import report_data
from ..src.log_report import log_report


class TestlogReportTitle(unittest.TestCase):
    """Testing report html file title"""

    def setUp(self):
        """Test data"""

        self.work_dir = Path.cwd()
        self.report_dir = "tests/t_report_title"
        self.report_rel_path = 'tests/t_report_title/report-2023.06.23.html'
        self.report_abs_path = os.path.join(self.work_dir, self.report_rel_path)
        self.report_dir_abs_path = os.path.join(self.work_dir, self.report_dir)
        self.report_date = datetime.strptime("20230623", '%Y%m%d').date()

    def tearDown(self):
        """Delete t_report dir"""

        if exists(self.report_dir_abs_path):
            shutil.rmtree(self.report_dir_abs_path)

    def test_report_html_title(self):
        """Testing report html title"""

        log_report(
            r_date=self.report_date,
            r_data=report_data,
            r_dir=self.report_dir
        )
        soup_file = open(self.report_abs_path, encoding="utf-8")
        # soup = BeautifulSoup(soup_file, features="html.parser")
        soup = BeautifulSoup(soup_file, "lxml")
        self.assertEqual(soup.title.get_text(), "rbui log analysis report")
        soup_file.close()


if __name__ == "__main__":
    unittest.main()

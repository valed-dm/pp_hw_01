"""Testing report html"""

import os
import shutil
import unittest
from datetime import datetime
from os.path import exists
from pathlib import Path

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from .t_reports.report_data import report_data
from ..src.log_report import log_report


class TestLogReportData:
    """Test columns, row_1 data"""

    table_cols: list = [
        'url', 'count', 'count_perc', 'time_avg', 'time_max', 'time_med', 'time_perc', 'time_sum'
    ]
    row_1: list = [
        '/agency/campaigns/6403173/banners/bulk_read/', '1', '1', '8.019', '8.019', '8.019', '12.506', '8.019'
    ]


class TestlogReportHTML(unittest.TestCase, TestLogReportData):
    """Testing report html file content"""

    def setUp(self):
        """Setup test"""

        self.work_dir = Path.cwd()
        self.report_dir = "tests/t_report"
        self.report_rel_path = 'tests/t_report/report-2023.06.23.html'
        self.report_abs_path = os.path.join(self.work_dir, self.report_rel_path)
        self.report_dir_abs_path = os.path.join(self.work_dir, self.report_dir)
        self.report_date = datetime.strptime("20230623", '%Y%m%d').date()
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(
        #     service=ChromiumService(
        #         ChromeDriverManager(
        #             chrome_type=ChromeType.CHROMIUM
        #         ).install()
        #     )
        # )
        self.driver = webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager()
                .install()
            )
        )

    def tearDown(self):
        """Clear selenium, delete t_report dir"""

        self.driver.close()
        if exists(self.report_dir_abs_path):
            shutil.rmtree(self.report_dir_abs_path)

    def test_report_html_cols_rows(self):
        """Testing html report content"""

        log_report(
            r_date=self.report_date,
            r_data=report_data,
            r_dir=self.report_dir
        )
        driver = self.driver
        driver.get("file://" + self.report_abs_path)
        columns = driver.find_elements(by=By.XPATH, value="//table/thead/tr/th")
        rows = driver.find_elements(by=By.XPATH, value="//table/tbody/tr")
        row_1 = rows[0]
        self.assertEqual(len(columns), 8)
        self.assertEqual(len(rows), 20)
        for column in columns:
            self.assertIn(column.text, self.table_cols)
            self.table_cols.remove(column.text)
        self.assertEqual(len(self.table_cols), 0)
        cols = row_1.find_elements(By.TAG_NAME, "td")
        for col in cols:
            self.assertIn(col.text, self.row_1)
            self.row_1.remove(col.text)
        self.assertEqual(len(self.row_1), 0)


if __name__ == "__main__":
    unittest.main()

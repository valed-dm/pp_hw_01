"""Testing log analyzer parsing capabilities"""

import unittest

from ..src.log_parser import Parser


class TestLogParser(unittest.TestCase):
    """Testing log analyzer parser"""

    def setUp(self):
        self.parser_gz = Parser(
            file="./tests/t_log_3/nginx-access-ui.log-20230623.gz",
            ext="gz",
            report_size=20
        )
        self.parser_log = Parser(
            file="./tests/t_log/nginx-access-ui.log-20230623.log",
            ext="log",
            report_size=20
        )

    def check_report(self, report):
        """Tests for report output"""

        self.assertEqual(len(report), 20)
        self.assertEqual(report[0]["url"], "/agency/campaigns/6403173/banners/bulk_read/")
        self.assertEqual(report[0]["time_avg"], 8.019)
        self.assertEqual(report[0]["time_perc"], 12.506)
        self.assertEqual(report[19]["url"], "/api/v2/banner/26614593")
        self.assertEqual(report[19]["time_avg"], 1.017)
        self.assertEqual(report[19]["time_perc"], 1.586)

    def test_log_parser_gz(self):
        """Checks a report resulted from an input log file with .gz extension processing"""
        with self.assertLogs("analyzer") as captured:
            report_gz = self.parser_gz.log_processor()
            self.check_report(report=report_gz)
            self.assertEqual(
                captured.records[0].getMessage(),
                "log file ./tests/t_log_3/nginx-access-ui.log-20230623.gz is being processed"
            )

    def test_log_parser_log(self):
        """Checks a report resulted from an input log file with .log extension processing"""

        with self.assertLogs("analyzer") as captured:
            report_log = self.parser_log.log_processor()
            self.check_report(report=report_log)
            self.assertEqual(
                captured.records[0].getMessage(),
                "log file ./tests/t_log/nginx-access-ui.log-20230623.log is being processed"
            )


if __name__ == "__main__":
    unittest.main()

"""Full testing a log analyzer configuration setup"""

import configparser
import tempfile
import unittest
from pathlib import Path

from ..src.helpers import create_arg_parser, log_cfg


class TestConfig(unittest.TestCase):
    """Testing log analyzer configuration provided by user and default values"""

    def setUp(self):
        """Create a temporary config file"""

        self.test_config = tempfile.NamedTemporaryFile(
            suffix='.ini'
        )
        config = configparser.ConfigParser(default_section='DEFAULT')
        config.set("DEFAULT", "LOG_DIR", "./test_log")
        config.set("DEFAULT", "REPORT_DIR", "./test_reports")
        config.set("DEFAULT", "REPORT_SIZE", "10")

        with Path(self.test_config.name).open("w", encoding="utf-8") as configfile:
            config.write(configfile)

    def tearDown(self):
        """Close the temporary config file"""
        self.test_config.close()

    def test_arg_parser(self):
        """Testing config path input from command line"""

        parser = create_arg_parser()
        args = parser.parse_args(["--config", "log.ini"])
        self.assertEqual(args.config, "log.ini")

    def test_config_creator(self):
        """Testing a log analyzer configuration creator ./helpers/log_cfg.py"""

        with self.assertLogs("analyzer") as captured:
            config = log_cfg(path=f"{self.test_config.name}")
            self.assertEqual(
                captured.records[0].getMessage(),
                f"app config file on path {self.test_config.name} is used."
            )
            self.assertEqual(config.log_dir, "./test_log")
            self.assertEqual(config.report_dir, "./test_reports")
            self.assertEqual(config.report_size, 10)

        with self.assertLogs("analyzer") as captured:
            config = log_cfg(path="log.pdf")
            self.assertEqual(
                captured.records[0].getMessage(),
                "app config file on path log.pdf is not valid. "
                "Default config values are used."
            )
            self.assertEqual(config.log_dir, "./log_default")
            self.assertEqual(config.report_dir, "./reports_default")
            self.assertEqual(config.report_size, 1000)

        with self.assertLogs("analyzer") as captured:
            config = log_cfg(path="log.ini")
            self.assertEqual(
                captured.records[0].getMessage(),
                "app config file on path log.ini does not exists. "
                "Default config values are used."
            )
            self.assertEqual(config.log_dir, "./log_default")
            self.assertEqual(config.report_dir, "./reports_default")
            self.assertEqual(config.report_size, 1000)

        with self.assertLogs("analyzer") as captured:
            config = log_cfg(path=None)
            self.assertEqual(
                captured.records[0].getMessage(),
                "Path to config file is not provided. "
                "Default config values are used."
            )
            self.assertEqual(config.log_dir, "./log_default")
            self.assertEqual(config.report_dir, "./reports_default")
            self.assertEqual(config.report_size, 1000)


if __name__ == '__main__':
    unittest.main()

"""Testing report template in log_src/log_report_template.py"""

from snapshottest import TestCase

from ..src.helpers import template_string


class TestReportTemplate(TestCase):
    """Testing report template string snapshot"""

    def test_report_template(self):
        """Testing report template string snapshot"""

        self.assertMatchSnapshot(template_string)

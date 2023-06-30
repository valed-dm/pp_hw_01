"""App report name creator"""


def report_name(log_date):
    """App report name creator"""

    date_str = log_date.strftime('%Y.%m.%d')
    return f"report-{date_str}.html"

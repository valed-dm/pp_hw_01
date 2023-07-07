"""Log parser args"""


class ParserData:
    """Log parser args"""

    def __init__(self, file, ext, report_size):
        self.log_file: str = file
        self.log_ext: str = ext
        self.report_size: str = report_size

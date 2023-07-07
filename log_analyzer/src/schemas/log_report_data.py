"""Default config for logs, reports"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseDate:
    """Base date for sorting purpose"""

    date = datetime.strptime("19000101", '%Y%m%d').date()


@dataclass
class Report(BaseDate):
    """Report config"""

    name: str = ""


@dataclass
class Log(BaseDate):
    """Log config"""

    name: str = ""
    ext: str = ""

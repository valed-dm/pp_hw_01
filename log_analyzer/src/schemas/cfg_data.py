"""Log analyzer default config values"""

from dataclasses import dataclass


@dataclass
class ConfigDefault:
    """App config default values"""

    log_dir: str = "./log_default"
    report_dir: str = "./reports_default"
    report_size: int = 1000

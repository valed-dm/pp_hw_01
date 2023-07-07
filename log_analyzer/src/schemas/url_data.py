"""Template for report data to be mined when parsing log"""

from dataclasses import dataclass, field

from .as_dict_redefined import Base


@dataclass
class ReqTimes(Base):
    """Time values template"""

    time_sum: float = 0
    time_perc: float = 0
    time_avg: float = 0
    time_max: float = 0
    time_med: float = 0
    req_times: list[float] = field(default_factory=list)
    # to exclude req_times from output dict
    _exclude = ["req_times"]


@dataclass
class UrlGroupedData(ReqTimes):
    """Final report data template"""

    url: str = ""
    count: int = 0
    count_perc: float = 0

    # I also tried this way to exclude req_times from dataclass output dictionary:
    # req_times: InitVar[list[float]] = field(default=list)

    # def __post_init__(self, req_times):
    #     self.req_times = req_times

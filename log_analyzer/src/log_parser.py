"""Log parser module"""

import gzip
import statistics

from .logging import Logging
from .schemas import ParserData, UrlGroupedData

logging = Logging("analyzer")
logger = logging.get_logger()


class Parser(ParserData):
    """Log parser"""

    def __init__(self, file, ext, report_size):
        super().__init__(file, ext, report_size)
        self.log_items_broken: int = 0
        self.log_items_qty: int = 0
        self.log_req_total_time: float = 0
        self.grouped_urls = {}
        self.report_raw: list[UrlGroupedData] = []
        self.report: list[dict] = []

    def report_creator(self):
        """Fills a report list with data"""

        for item in self.report_raw:
            item.count_perc = round((item.count / self.log_items_qty) * 100, 3)
            item.time_perc = round((item.time_sum / self.log_req_total_time) * 100, 3)
            item.time_avg = round((item.time_sum / item.count), 3)
            item.time_med = round(statistics.median(item.req_times), 3)
            item.time_sum = round(item.time_sum, 3)
            self.report.append(item._asdict())

    def python_process_log(self):
        """Parse log's urls and it's data"""

        logger.info("log file %s is being processed", self.log_file)
        with (gzip.open if self.log_ext == "gz" else open)(
                self.log_file,
                'rt',
                encoding='utf-8'
        ) as log:
            for line in log:
                line_split = line.split(' ')
                if not line_split[7].startswith("/") and not line_split[7].startswith("http"):
                    self.log_items_broken += 1
                else:
                    url = str(line_split[7])
                    req_time = float(line.rsplit(" ", 1)[1].rstrip("\n"))
                    self.log_items_qty += 1
                    self.log_req_total_time += req_time
                    if url not in self.grouped_urls:
                        self.grouped_urls[f"{url}"] = UrlGroupedData(
                            url=url,
                            count=1,
                            time_sum=req_time,
                            time_max=req_time,
                            req_times=[req_time]
                        )
                    else:
                        self.grouped_urls[f"{url}"].count += 1
                        self.grouped_urls[f"{url}"].time_sum += req_time
                        self.grouped_urls[f"{url}"].time_max = max(
                            self.grouped_urls[f"{url}"].time_max, req_time
                        )
                        self.grouped_urls[f"{url}"].req_times.append(req_time)

        data_damaged_perc = round(self.log_items_broken / self.log_items_qty * 100, 4)
        data_error_perc_acceptable = 0.001

        if self.log_items_qty == 0:
            msg = f"log file {self.log_file} is empty"
            return msg
        if data_damaged_perc > data_error_perc_acceptable:
            msg = f"data broken {data_damaged_perc}% exceeds limit {data_error_perc_acceptable}%"
            return msg

        res_filtered = {k: v for k, v in self.grouped_urls.items() if v.count > 0}
        self.report_raw = sorted(
            res_filtered.values(),
            key=lambda item: item.time_sum,
            reverse=True
        )[:self.report_size]

        self.report_creator()
        logger.info(
            "log file %s contains %0.4f %% of data broken"
            , self.log_file
            , data_damaged_perc
        )

        return self.report

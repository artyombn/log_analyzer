import gzip

from ..log_parsing.parse_log_line import parse_log_line


def gzip_handler(log_file_name, report_size, logs_dir):

    log_data = []

    with gzip.open(
        f"{logs_dir}/{log_file_name}", mode="rt", encoding="utf-8"
    ) as log_file:
        for i, line in enumerate(log_file, start=1):
            if i >= report_size + 1:
                break
            log_data.append(parse_log_line(line))

    if not log_data:
        return "No valid log data found"
    return log_data

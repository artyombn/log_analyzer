import gzip

from ..log_parsing.parse_log_line import parse_log_line


def gzip_handler(log_file_name, logs_dir):

    log_data = []

    try:
        with gzip.open(
            f"{logs_dir}/{log_file_name}", mode="rt", encoding="utf-8"
        ) as log_file:
            for line in log_file:
                z = parse_log_line(line)

                if not z:
                    continue

                log_data.append(z)

    except FileNotFoundError:
        return "No logs"
    except PermissionError:
        return "No logs"

    if not log_data:
        return "No logs"
    return log_data

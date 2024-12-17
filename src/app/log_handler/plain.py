from ..log_parsing.parse_log_line import parse_log_line


def plain_handler(log_file_name, logs_dir):

    log_data = []
    try:
        with open(
            f"{logs_dir}/{log_file_name}", mode="rt", encoding="utf-8"
        ) as log_file:
            for line in log_file:
                log_data.append(parse_log_line(line))
    except FileNotFoundError:
        return "No logs"
    except PermissionError:
        return "No logs"

    if not log_data:
        return "No logs"
    return log_data

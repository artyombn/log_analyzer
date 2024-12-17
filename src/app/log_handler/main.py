from ..get_last_log import get_last_log_file
from ..processed_logs import load_processed_logs
from .gzip import gzip_handler
from .plain import plain_handler


def handler(config):

    log_dir = config["LOG_DIR"]
    report_dir = config["REPORT_DIR"]

    log_file_name = get_last_log_file(log_dir)

    processed_logs = load_processed_logs(report_dir)

    if log_file_name[0] in processed_logs:
        return "Sys.exit"

    if log_file_name[1] and log_file_name != "No logs":
        return gzip_handler(log_file_name[0], log_dir)
    if not log_file_name[1] and log_file_name != "No logs":
        return plain_handler(log_file_name[0], log_dir)
    return "No logs"

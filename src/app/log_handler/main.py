from ..get_last_log import get_last_log_file
from .gzip import gzip_handler
from .plain import plain_handler


def handler(config):

    log_dir = config["LOG_DIR"]

    log_file_name = get_last_log_file(log_dir)

    if log_file_name[1] and log_file_name != "No logs":
        return gzip_handler(log_file_name[0], log_dir)
    if not log_file_name[1] and log_file_name != "No logs":
        return plain_handler(log_file_name[0], log_dir)
    raise FileNotFoundError("No log file or directory")

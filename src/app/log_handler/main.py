from ..get_last_log import get_last_log_file, logs_dir
from .gzip import gzip_handler
from .plain import plain_handler

log_file_name = get_last_log_file()


def handler():
    if log_file_name[1] and log_file_name != "No logs":
        return gzip_handler(log_file_name[0], logs_dir)
    if not log_file_name[1] and log_file_name != "No logs":
        return plain_handler(log_file_name[0], logs_dir)
    return "No logs"


Z = handler()

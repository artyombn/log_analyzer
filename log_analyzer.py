# log_format ui_short '$remote_addr  $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';


import argparse

from src.app.log_handler.main import handler
from src.app.log_parsing.collect_stats import collect_statistics
from src.app.log_parsing.generate_report import generate_report
from src.config.config import config as default_config
from src.config.load_config import load_config
from src.config.merge_config import merge_config


def parse_args():
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument(
        "--config",
        type=str,
        default="src/config/config.json",
        help="Your config.json file",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    file_config = load_config(args.config)
    report_config = merge_config(default_config, file_config)
    log_handler = handler(report_config)
    stats = collect_statistics(log_handler, report_config)
    report = generate_report(stats, report_config)


if __name__ == "__main__":
    main()

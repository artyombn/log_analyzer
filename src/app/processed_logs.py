import json
from pathlib import Path


def load_processed_logs(report_dir):
    processed_logs_file = Path(report_dir) / "processed_logs.json"
    if not processed_logs_file.exists():
        processed_logs_file.parent.mkdir(parents=True, exist_ok=True)
        with open(processed_logs_file, "w", encoding="utf-8") as f:
            json.dump({}, f)

    with open(processed_logs_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_processed_log(report_dir, log_file_name, report_file_name):
    processed_logs_file = Path(report_dir) / "processed_logs.json"
    processed_logs = load_processed_logs(report_dir)
    processed_logs[log_file_name] = report_file_name
    with open(processed_logs_file, "w", encoding="utf-8") as f:
        json.dump(processed_logs, f, indent=4)

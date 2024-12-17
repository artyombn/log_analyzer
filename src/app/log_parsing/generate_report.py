import json
from datetime import datetime
from pathlib import Path

from src.app.get_last_log import get_last_log_file
from src.app.processed_logs import save_processed_log

root = Path(__file__).parent.parent
project_root = root.parent.parent
template_file = root / "templates" / "report.html"

current_date = datetime.now().strftime("%Y.%m.%d")
REPORT_NAME = f"report-{current_date}.html"


def generate_report(stats, config):

    json_str = json.dumps(stats)

    with open(template_file, "r", encoding="utf-8") as template:
        template_content = template.read()

    html_content = template_content.replace("{{ table_json }}", json_str)

    output_folder = project_root / config["REPORT_DIR"]
    output_folder.mkdir(parents=True, exist_ok=True)

    output_path = output_folder / REPORT_NAME

    with open(output_path, "w", encoding="utf-8") as report:
        report.write(html_content)
    last_log_file, _ = get_last_log_file(config["LOG_DIR"])

    save_processed_log(config["REPORT_DIR"], last_log_file, REPORT_NAME)

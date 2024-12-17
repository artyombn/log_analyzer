import re
from pathlib import Path


def get_last_log_file(logs_dir):

    logs_dir = Path(logs_dir) if isinstance(logs_dir, str) else logs_dir
    try:
        files = [f.name for f in logs_dir.iterdir() if f.is_file()]

        file_dates = {}

        for f in files:
            date = re.findall(r"\d+", f)
            if not date:
                continue

            try:
                date_int = int("".join(date))
            except ValueError:
                continue

            gz = ".gz" in f
            file_dates[date_int] = gz

        if not file_dates:
            return "No logs"

        last_file_date = max(file_dates)

        if file_dates[last_file_date]:
            last_file_name = f"nginx-access-ui.log-{last_file_date}.gz"
        else:
            last_file_name = f"nginx-access-ui.log-{last_file_date}"

        return last_file_name, file_dates[last_file_date]

    except FileNotFoundError:
        return "No logs"

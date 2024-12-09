import re
from pathlib import Path


logs_dir = Path(__file__).resolve().parent.parent.parent / "logs"

def get_last_log_file():
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

        GZ = ".gz" in f
        file_dates[date_int] = GZ

    try:
        last_file_date = max(file_dates)

        if file_dates[last_file_date]:
            last_file_name = f"nginx-access-ui.log-{last_file_date}.gz"
        else:
            last_file_name = f"nginx-access-ui.log-{last_file_date}"

        return last_file_name, file_dates[last_file_date]

    except ValueError:
        return "No logs"
    except Exception as e:
        return str(e)


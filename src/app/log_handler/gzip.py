import gzip


def gzip_handler(log_file_name, logs_dir):
    with gzip.open(
        f"{logs_dir}/{log_file_name}", mode="rt", encoding="utf-8"
    ) as log_file:
        for i, line in enumerate(log_file):
            if i >= 10:
                break
            print(line.strip())

    print(f"GZIP_HANDLER done")

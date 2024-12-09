def plain_handler(log_file_name, report_size, logs_dir):
    with open(f"{logs_dir}/{log_file_name}", mode="rt", encoding="utf-8") as log_file:
        for i, line in enumerate(log_file):
            if i >= report_size:
                break
            print(line.strip())
    print("PLAIN_HANDLER done")
    print(f"Log_file_name = {log_file_name}")
    print(f"report_size = {report_size}")
    print(f"logs_dir = {logs_dir}")

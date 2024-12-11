from statistics import median


def collect_statistics(log_data, config):
    stats = {}

    report_size = config["REPORT_SIZE"]

    for log in log_data:
        url = log["url"]
        request_time = log["request_time"]

        if url not in stats:
            stats[url] = {
                "count": 0,
                "time_sum": 0,
                "time_max": 0,
                "times": [],
            }

        stats[url]["count"] += 1
        stats[url]["time_sum"] = round((stats[url]["time_sum"] + request_time), 3)
        stats[url]["time_max"] = round((max(stats[url]["time_max"], request_time)), 3)
        stats[url]["times"].append(request_time)

    total_count = sum(i["count"] for i in stats.values())
    total_time = sum(i["time_sum"] for i in stats.values())

    stats_list = []
    for url, res in stats.items():
        res["count_perc"] = round(((res["count"] / total_count) * 100), 3)
        res["time_perc"] = round(((res["time_sum"] / total_time) * 100), 3)
        res["time_avg"] = round((res["time_sum"] / res["count"]), 3)
        res["time_med"] = round((median(res["times"])), 3)
        del res["times"]
        stats_list.append({"url": url, **res})

    return sorted(stats_list, key=lambda x: x["time_sum"], reverse=True)[:report_size]

from statistics import median


def collect_statistics(log_data):
    stats = {}

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
        stats[url]["time_sum"] += request_time
        stats[url]["time_max"] = max(stats[url]["time_max"], request_time)
        stats[url]["times"].append(request_time)

    total_count = sum(i["count"] for i in stats.values())
    total_time = sum(i["time_sum"] for i in stats.values())

    for url, res in stats.items():
        res["count_perc"] = (res["count"] / total_count) * 100
        res["time_perc"] = (res["time_sum"] / total_time) * 100
        res["time_avg"] = res["time_sum"] / res["count"]
        res["time_med"] = median(res["times"])
        del res["times"]

    return stats

import gzip
from contextlib import nullcontext as does_not_raise

import pytest

logs_content = [
    {"url": "/api/v2/banner/25019354", "request_time": 0.390},
    {
        "url": "/api/1/photogenic_banners/list/?server_name=WIN7RB4",
        "request_time": 0.133,
    },
    {"url": "/api/v2/banner/16852664", "request_time": 0.199},
    {"url": "/api/v2/slot/4705/groups", "request_time": 0.704},
    {"url": "/api/v2/internal/banner/24294027/info", "request_time": 0.146},
    {"url": "/api/v2/group/1769230/banners", "request_time": 0.628},
    {
        "url": "/api/v2/group/7786679/statistic/sites/?date_type=day&date_from=2017-06-28&date_to=2017-06-28",
        "request_time": 0.067,
    },
    {"url": "/api/v2/banner/1717161", "request_time": 0.138},
    {"url": "/export/appinstall_raw/2017-06-29/", "request_time": 0.003},
    {"url": "/api/v2/slot/4822/groups", "request_time": 0.157},
]

parametrize_for_gzip = [
    (
        ["tests-nginx-access-ui.log-20170628.gz", True],
        "./logs",
        logs_content,
        does_not_raise(),
    ),
    (
        ["tests-nginx-access-ui.log-20170628", False],
        "./logs",
        logs_content,
        pytest.raises(gzip.BadGzipFile),
    ),
    (
        ["wrong-name-nginx-access-ui.log-20170628", False],
        "./logs",
        "No logs",
        pytest.raises(FileNotFoundError),
    ),
    (
        "No logs",
        "./logs",
        "No logs",
        pytest.raises(FileNotFoundError),
    ),
    (
        "No logs",
        "./other_logs",
        "No logs",
        pytest.raises(FileNotFoundError),
    ),
]

parametrize_for_plain = [
    (
        ["tests-nginx-access-ui.log-20170628.gz", True],
        "./logs",
        logs_content,
        pytest.raises(UnicodeDecodeError),
    ),
    (
        ["tests-nginx-access-ui.log-20170628", False],
        "./logs",
        logs_content,
        does_not_raise(),
    ),
    (
        ["wrong-name-nginx-access-ui.log-20170628", False],
        "./logs",
        "No logs",
        pytest.raises(FileNotFoundError),
    ),
    (
        "No logs",
        "./logs",
        "No logs",
        pytest.raises(FileNotFoundError),
    ),
    (
        "No logs",
        "./other_logs",
        "No logs",
        pytest.raises(FileNotFoundError),
    ),
]


parametrize_for_handler = [
    (
        ["tests-nginx-access-ui.log-20170628.gz", True],
        {"LOG_DIR": "./logs"},
        logs_content,
        does_not_raise(),
    ),
    (
        ["tests-nginx-access-ui.log-20170628", False],
        {"LOG_DIR": "./logs"},
        logs_content,
        does_not_raise(),
    ),
    (
        ["wrong-name-nginx-access-ui.log-20170628", False],
        {"LOG_DIR": "./logs"},
        "No logs",
        pytest.raises(FileNotFoundError),
    ),
    (
        "No logs",
        {"LOG_DIR": "./logs"},
        "No logs",
        does_not_raise(),
    ),
    (
        "No logs",
        {"LOG_DIR": "./other_logs"},
        "No logs",
        does_not_raise(),
    ),
]

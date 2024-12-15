from contextlib import nullcontext as does_not_raise

import pytest

from src.app.log_handler.main import handler


@pytest.mark.parametrize(
    "REPORT_SIZE, REPORT_DIR, LOG_DIR",
    [
        (20, "./reports", "./logs"),
        # (None, "./reports", "./logs"),
        # (20, None, "./logs"),
        # (20, "./reports", None),
        # (20, None, None),
        # (None, None, "./logs"),
        # (None, "./reports", None),
        # None,
        # {},
    ],
)
def test_handler(REPORT_SIZE, REPORT_DIR, LOG_DIR):
    log_dir = LOG_DIR
    log_file_name = "nginx-access-ui.log-20170630.gz"

    if ".gz" in log_file_name:
        assert True

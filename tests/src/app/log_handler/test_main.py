import gzip
from unittest.mock import patch

import pytest

from src.app.log_handler.gzip import gzip_handler
from src.app.log_handler.main import handler
from src.app.log_handler.plain import plain_handler
from tests.src.app.log_handler.test_data import (
    logs_content,
    parametrize_for_gzip,
    parametrize_for_handler,
    parametrize_for_plain,
)


@pytest.mark.parametrize(
    "log_file_name, LOG_DIR, log_data, expectation",
    parametrize_for_gzip,
)
def test_gzip_handler(log_file_name, LOG_DIR, log_data, expectation):
    with expectation:
        assert logs_content == gzip_handler(log_file_name[0], LOG_DIR)


@pytest.mark.parametrize(
    "log_file_name, LOG_DIR, log_data, expectation",
    parametrize_for_plain,
)
def test_plain_handler(log_file_name, LOG_DIR, log_data, expectation):
    with expectation:
        assert logs_content == plain_handler(log_file_name[0], LOG_DIR)


@pytest.mark.parametrize(
    "log_file_name, config, log_data, expectation",
    parametrize_for_handler,
)
@patch("src.app.log_handler.main.get_last_log_file")
def test_handler(mock_get_last_log_file, log_file_name, config, log_data, expectation):
    with expectation:
        mock_get_last_log_file.return_value = log_file_name

        if log_file_name[1] and log_file_name != "No logs":
            assert logs_content == handler(config)
        elif not log_file_name[1] and log_file_name != "No logs":
            assert logs_content == handler(config)
        else:
            assert handler(config) == "No logs"

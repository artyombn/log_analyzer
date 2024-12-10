import re

LOG_PATTERN = re.compile(
    r"(?P<ip>\S+)s* (?P<identifier>\S+)? \s* - \[(?P<time>[^\]]+)] "
    r'"(?P<method>GET|POST) (?P<url>\S+) HTTP/\S+" '
    r'(?P<status>\d+) (?P<size>\d+) "[^"]*" "(?P<user_agent>[^"]*)" '
    r'"-" "[^"]*" "[^"]*" (?P<request_time>\d+\.\d+)'
)


def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        return {
            "url": match.group("url"),
            "request_time": float(match.group("request_time")),
        }
    return None

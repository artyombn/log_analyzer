import json
import os


def load_config(config_path):
    if not os.path.exists(config_path):
        return "No config file"

    try:
        with open(config_path, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return "JSON is not valid"

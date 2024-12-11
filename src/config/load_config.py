import json
import os


def load_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError("Config file is not found")

    try:
        with open(config_path, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError("JSON is not valid") from exc

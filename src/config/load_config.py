import os
import sys
import json


def load_config(config_path):
    if not os.path.exists(config_path):
        return f"No config file"

    try:
        with open(config_path, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return f"JSON is not valid"
    except Exception as e:
        return f"Error: {e}"

def merge_config(default_config, file_config):
    merged_config = default_config.copy()

    if isinstance(file_config, dict):
        merged_config.update(file_config)

    return merged_config

"""pd.read_csv"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """pd.read_csv"""
    if 'path' not in settings:
        raise Exception('Missing path param')

    prefix = settings['local_path_prefix'] if 'local_path_prefix' in settings else ''

    dfs[settings['df']] = pd.read_csv(
        prefix + settings['path'],
        low_memory=False,
    )

    return dfs

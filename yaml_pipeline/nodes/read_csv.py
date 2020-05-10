"""pd.read_csv"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """pd.read_csv"""
    if 'path' not in settings:
        raise Exception('Missing path param')

    dfs[settings['df']] = pd.read_csv(
        settings['path_prefix'] + settings['path'],
        low_memory=False,
    )

    return dfs
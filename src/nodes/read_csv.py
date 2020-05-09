"""pd.read_csv"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """pd.read_csv"""
    name = settings['name'] if 'name' in settings else 'default'

    if 'path' not in settings:
        raise Exception('Missing path param')

    dfs[name] = pd.read_csv(
        settings['path'],
        low_memory=False,
    )

    return dfs

"""df.to_csv()"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """df.to_csv()"""
    df = settings['df'] if 'df' in settings else 'default'

    if df not in dfs:
        raise Exception('No df specified')

    if 'path' not in settings:
        raise Exception('No path param')

    dfs[df].to_csv(
        settings['path'],
        index=False,
    )

    return dfs

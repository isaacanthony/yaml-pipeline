"""df.to_csv()"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """df.to_csv()"""
    if 'path' not in settings:
        raise Exception('Missing path param')

    dfs[settings['df']].to_csv(
        settings['path'],
        index=False,
    )

    return dfs

"""df.rename(columns={})"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """df.rename(columns={})"""
    if 'columns' not in settings:
        raise Exception('Missing columns param')

    dfs[settings['df']] = dfs[settings['df']].rename(columns=settings['columns'])
    return dfs

"""df.drop(columns=[])"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """df = df.drop(columns=[])"""
    if 'columns' not in settings:
        raise Exception('Missing columns param')

    dfs[settings['df']] = dfs[settings['df']].drop(columns=settings['columns'])
    return dfs

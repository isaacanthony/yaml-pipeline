"""df.rename(columns={})"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """df.rename(columns={})"""
    df = settings['df'] if 'df' in settings else 'default'

    if df not in dfs:
        raise Exception('Missing df param')

    if 'columns' not in settings:
        raise Exception('Missing columns param')

    dfs[df] = dfs[df].rename(columns=settings['columns'])
    return dfs

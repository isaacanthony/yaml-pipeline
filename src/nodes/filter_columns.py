"""df[{}]"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """df[{}]"""
    if 'columns' not in settings:
        raise Exception('Missing columns param')

    dfs[settings['df']] = dfs[settings['df']][settings['columns']]
    return dfs

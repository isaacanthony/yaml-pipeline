"""np.floor()"""
import numpy as np


def run(dfs: dict, settings: dict) -> dict:
    """np.floor()"""
    df = dfs[settings['df']]

    if 'columns' in settings:
        for col in settings['columns']:
            df[col] = df[col].apply(np.floor)

    else:
        df = df.apply(np.floor)

    dfs[settings['df']] = df
    return dfs

"""np.ceil()"""
import numpy as np


def run(dfs: dict, settings: dict) -> dict:
    """np.ceil()"""
    df = dfs[settings['df']]

    if 'columns' in settings:
        for col in settings['columns']:
            df[col] = df[col].apply(np.ceil)

    else:
        df = df.apply(np.ceil)

    dfs[settings['df']] = df
    return dfs

"""df.head()"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """df.head()"""
    df = settings['df'] if 'df' in settings else 'default'

    if df not in dfs:
        raise Exception('Invalid df to head')

    df = dfs[df]

    print()
    print(df.head())
    print()

    return dfs

"""df.head()"""
import pandas as pd


def run(dfs: dict, settings: dict) -> pd.DataFrame:
    """df.head()"""
    df = settings['df'] if 'df' in settings else 'default'

    if df not in dfs:
        raise Exception('Missing df param')

    print()
    print(dfs[df].head())
    print()

    return dfs

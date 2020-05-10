"""df.head()"""
import pandas as pd


def run(dfs: dict, settings: dict) -> pd.DataFrame:
    """df.head()"""
    print()
    print(dfs[settings['df']].head())
    print()

    return dfs

"""df2 = df1.copy()"""


def run(dfs: dict, settings: dict) -> dict:
    """df2 = df1.copy()"""
    if 'dfs' not in settings:
        raise Exception('Missing dfs param')

    for old_df, new_df in settings['dfs'].items():
        dfs[new_df] = dfs[old_df].copy()

    return dfs

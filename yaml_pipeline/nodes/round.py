"""df[[]].round()"""


def run(dfs: dict, settings: dict) -> dict:
    """df[[]].round()"""
    decimals = settings['decimals'] if 'decimals' in settings else 0
    df = dfs[settings['df']]

    if 'columns' in settings:
        df[settings['columns']] = df[settings['columns']].round(decimals)
    else:
        df = df.round(decimals)

    dfs[settings['df']] = df
    return dfs

"""df[{}] = df[{}].astype({})"""


def run(dfs: dict, settings: dict) -> dict:
    """df[{}] = df[{}].astype({})"""
    if 'columns' not in settings:
        raise Exception('Missing columns param')

    dfs[settings['df']] = dfs[settings['df']].astype(settings['columns'])
    return dfs

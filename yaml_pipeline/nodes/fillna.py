"""df.fillna()"""


def run(dfs: dict, settings: dict) -> dict:
    """df.fillna()"""
    if 'value' not in settings:
        raise Exception('Missing value param')

    df = dfs[settings['df']]

    if 'columns' in settings:
        for col in settings['columns']:
            df[col] = df[col].fillna(settings['value'])

    else:
        df = df.fillna(settings['value'])

    dfs[settings['df']] = df
    return dfs

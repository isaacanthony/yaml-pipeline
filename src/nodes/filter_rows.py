"""df[df[{}] == {}]"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """df[df[{}] == {}]"""
    for setting in ['filter', 'column', 'value']:
        if setting not in settings:
            raise Exception(f"Missing {setting} param")

    df = dfs[settings['df']]
    column = settings['column']
    filter = settings['filter']
    value = settings['value']

    # POSITIVE MATCHES
    if filter == 'contains':
        df = df[df[column].str.contains(value, regex=True)]

    elif filter == 'eq':
        df = df[df[column] == value]

    elif filter == 'gt':
        df = df[df[column] > value]

    elif filter == 'gte':
        df = df[df[column] >= value]

    elif filter == 'in':
        df = df[df[col].isin(set(value))]

    elif filter == 'startswith':
        df = df[df[column].str.startswith(value)]

    elif filter == 'lt':
        df = df[df[column] < value]

    elif filter == 'lte':
        df = df[df[column] <= value]

    # NEGATIVE MATCHES
    elif filter == 'not.contains':
        df = df[~df[column].str.contains(value, regex=True)]

    elif filter == 'not.eq':
        df = df[df[column] != value]

    elif filter == 'not.in':
        df = df[~df[col].isin(set(value))]

    else:
        raise Exception('Invalid filter param')

    dfs[settings['df']] = df.copy()
    return dfs

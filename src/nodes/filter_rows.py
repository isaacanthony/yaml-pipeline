"""df[df[{}] == {}]"""


# pylint: disable=too-many-branches
def run(dfs: dict, settings: dict) -> dict:
    """df[df[{}] == {}]"""
    for setting in ['filter', 'column', 'value']:
        if setting not in settings:
            raise Exception(f"Missing {setting} param")

    df = dfs[settings['df']]
    column = settings['column']
    fltr = settings['filter']
    value = settings['value']

    # POSITIVE MATCHES
    if fltr == 'contains':
        df = df[df[column].str.contains(value, regex=True)]

    elif fltr == 'eq':
        df = df[df[column] == value]

    elif fltr == 'gt':
        df = df[df[column] > value]

    elif fltr == 'gte':
        df = df[df[column] >= value]

    elif fltr == 'in':
        df = df[df[column].isin(set(value))]

    elif fltr == 'startswith':
        df = df[df[column].str.startswith(value)]

    elif fltr == 'lt':
        df = df[df[column] < value]

    elif fltr == 'lte':
        df = df[df[column] <= value]

    # NEGATIVE MATCHES
    elif fltr == 'not.contains':
        df = df[~df[column].str.contains(value, regex=True)]

    elif fltr == 'not.eq':
        df = df[df[column] != value]

    elif fltr == 'not.in':
        df = df[~df[column].isin(set(value))]

    else:
        raise Exception('Invalid filter param')

    dfs[settings['df']] = df.copy()
    return dfs

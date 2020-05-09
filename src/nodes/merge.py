"""df1 = df1.merge(d2)"""


def run(dfs: dict, settings: dict) -> dict:
    """df1 = df1.merge(d2)"""
    if 'dfs' not in settings:
        raise Exception('Missing dfs param')

    if len(settings['dfs']) != 2:
        raise Exception('Invalid dfs param')

    both_on = settings['on'] if 'on' in settings else None
    left_on = settings['left_on'] if 'left_on' in settings else None
    right_on = settings['right_on'] if 'right_on' in settings else None
    how = settings['how'] if 'how' in settings else 'inner'
    suffixes = settings['suffixes'] if 'suffixes' in settings else ['_x', '_y']

    dfs[settings['df']] = dfs[settings['dfs'][0]].merge(
        dfs[settings['dfs'][1]],
        how=how,
        on=both_on,
        left_on=left_on,
        right_on=right_on,
        suffixes=tuple(suffixes),
    )

    return dfs

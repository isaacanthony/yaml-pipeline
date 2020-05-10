"""Drop dfs from dfs"""


def run(dfs: dict, settings: dict) -> dict:
    """Drop df from dfs"""
    if 'dfs' not in settings:
        raise Exception('Missing dfs param')

    for df in settings['dfs']:
        if df not in dfs:
            raise Exception('Invalid dfs param')

        dfs.pop(df)

    return dfs

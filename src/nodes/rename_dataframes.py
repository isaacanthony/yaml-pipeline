"""Rename df in dfs"""


def run(dfs: dict, settings: dict) -> dict:
    """Rename df in dfs"""
    if 'dfs' not in settings:
        raise Exception('Missing dfs param')

    for old_name, new_name in settings['dfs'].items():
        if old_name not in dfs:
            raise Exception('Invalid dfs param')

        dfs[new_name] = dfs.pop(old_name)

    return dfs

"""os.mkdir"""
from os import mkdir


def run(dfs: dict, settings: dict) -> dict:
    """os.mkdir"""
    if 'dirs' not in settings:
        raise Exception('Missing dirs param')

    for new_dir in settings['dirs']:
        mkdir(settings['local_prefix'] + new_dir)

    return dfs

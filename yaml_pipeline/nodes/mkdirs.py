"""os.mkdir"""
from os import mkdir, path


def run(dfs: dict, settings: dict) -> dict:
    """os.mkdir"""
    if 'dirs' not in settings:
        raise Exception('Missing dirs param')

    for new_dir in settings['dirs']:
        if path.exists(settings['local_prefix'] + new_dir):
            if 'logger' in settings:
                settings['logger'].info("%s already exists", new_dir)
        else:
            mkdir(settings['local_prefix'] + new_dir)

    return dfs

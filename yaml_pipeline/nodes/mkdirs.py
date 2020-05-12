"""os.mkdir"""
from os import mkdir, path


def run(dfs: dict, settings: dict) -> dict:
    """os.mkdir"""
    if 'dirs' not in settings:
        raise Exception('Missing dirs param')

    prefix = settings['local_path_prefix'] if 'local_path_prefix' in settings else ''

    for new_dir in settings['dirs']:
        if path.exists(prefix + new_dir):
            if 'logger' in settings:
                settings['logger'].info("Directory already exists (%s)", new_dir)
        else:
            mkdir(prefix + new_dir)

    return dfs

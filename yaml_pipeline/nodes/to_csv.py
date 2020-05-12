"""df.to_csv()"""


def run(dfs: dict, settings: dict) -> dict:
    """df.to_csv()"""
    if 'path' not in settings:
        raise Exception('Missing path param')

    prefix = settings['local_path_prefix'] if 'local_path_prefix' in settings else ''

    dfs[settings['df']].to_csv(
        prefix + settings['path'],
        index=False,
    )

    return dfs

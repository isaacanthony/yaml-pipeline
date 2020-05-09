"""df.to_csv()"""


def run(dfs: dict, settings: dict) -> dict:
    """df.to_csv()"""
    if 'path' not in settings:
        raise Exception('Missing path param')

    dfs[settings['df']].to_csv(
        settings['path_prefix'] + settings['path'],
        index=False,
    )

    return dfs

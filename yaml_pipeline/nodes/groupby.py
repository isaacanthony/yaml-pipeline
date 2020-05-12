"""df.groupby().reset_index()"""


def run(dfs: dict, settings: dict) -> dict:
    """df.groupby().reset_index()"""
    for setting in ['agg', 'by']:
        if setting not in settings:
            raise Exception(f"Missing {setting} param")

    dfs[settings['df']] = dfs[settings['df']].groupby(settings['by']) \
        .agg(settings['agg']) \
        .reset_index()

    return dfs

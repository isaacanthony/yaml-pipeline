"""df.drop_duplicates(subset={})"""


def run(dfs: dict, settings: dict) -> dict:
    """df.drop_duplicates(subset={})"""
    subset = settings['subset'] if 'subset' in settings else None
    keep = settings['keep'] if 'keep' in settings else 'first'

    dfs[settings['df']] = dfs[settings['df']].drop_duplicates(
        subset=subset,
        keep=keep,
        ignore_index=True,
    )

    return dfs

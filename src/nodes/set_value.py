"""df[{}] = {}"""


def run(dfs: dict, settings: dict) -> dict:
    """df[{}] = {}"""
    for setting in ['column', 'value']:
        if setting not in settings:
            raise Exception(f"Missing {setting} param")

    df = dfs[settings['df']]
    df[settings['column']] = eval(str(settings['value']))  # pylint: disable=eval-used
    dfs[settings['df']] = df
    return dfs

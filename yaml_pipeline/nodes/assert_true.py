"""assert {value}"""


def run(dfs: dict, settings: dict) -> dict:
    """assert {value}"""
    if 'value' not in settings:
        raise Exception('Missing value param')

    # pylint: disable=eval-used,unused-variable
    df = dfs[settings['df']]
    assert eval(str(settings['value']))
    return dfs

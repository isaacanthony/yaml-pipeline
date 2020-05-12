"""list(df)"""


def run(dfs: dict, settings: dict) -> dict:
    """list(df)"""
    print()
    print("\n".join(list(dfs[settings['df']])))
    print()

    return dfs

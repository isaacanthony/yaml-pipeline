"""df.head()"""


def run(dfs: dict, settings: dict) -> dict:
    """df.head()"""
    num = settings['n'] if 'n' in settings else 5

    print()
    print(dfs[settings['df']].head(num))
    print()

    return dfs

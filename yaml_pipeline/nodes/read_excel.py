"""pd.read_excel()"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """pd.read_excel()"""
    for setting in ['path', 'sheet_name']:
        if setting not in settings:
            raise Exception(f"Missing {setting} param")

    skiprows = settings['skiprows'] if 'skiprows' in settings else None

    dfs[settings['df']] = pd.read_excel(
        settings['path'],
        sheet_name=settings['sheet_name'],
        skiprows=skiprows,
    )

    return dfs

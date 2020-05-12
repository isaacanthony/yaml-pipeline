"""pd.read_excel()"""
import pandas as pd


def run(dfs: dict, settings: dict) -> dict:
    """pd.read_excel()"""
    if 'path' not in settings:
        raise Exception('Missing path param')

    prefix = settings['local_path_prefix'] if 'local_path_prefix' in settings else ''
    sheet_name = settings['sheet_name'] if 'sheet_name' in settings else 0
    skiprows = settings['skiprows'] if 'skiprows' in settings else None

    dfs[settings['df']] = pd.read_excel(
        prefix + settings['path'],
        sheet_name=sheet_name,
        skiprows=skiprows,
    )

    return dfs

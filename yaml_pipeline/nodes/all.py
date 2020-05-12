"""Run a node"""
from yaml_pipeline.nodes import \
    astype, \
    ceil, \
    copy_dataframes, \
    download_s3, \
    drop_columns, \
    drop_dataframes, \
    drop_duplicates, \
    fillna, \
    filter_columns, \
    filter_rows, \
    floor, \
    groupby, \
    head, \
    len as len_dataframe, \
    list_columns, \
    merge, \
    mkdirs, \
    read_csv, \
    read_excel, \
    rename_columns, \
    rename_dataframes, \
    round as round_columns, \
    set_value, \
    to_csv

NODES = {
    'astype': astype,
    'ceil': ceil,
    'copy_dataframes': copy_dataframes,
    'download_s3': download_s3,
    'drop_columns': drop_columns,
    'drop_dataframes': drop_dataframes,
    'drop_duplicates': drop_duplicates,
    'fillna': fillna,
    'filter_columns': filter_columns,
    'filter_rows': filter_rows,
    'groupby': groupby,
    'floor': floor,
    'head': head,
    'len': len_dataframe,
    'list_columns': list_columns,
    'merge': merge,
    'mkdirs': mkdirs,
    'read_csv': read_csv,
    'read_excel': read_excel,
    'rename_columns': rename_columns,
    'rename_dataframes': rename_dataframes,
    'round': round_columns,
    'set_value': set_value,
    'to_csv': to_csv,
}


def run(dfs: dict, settings: dict) -> dict:
    """Run a node"""
    settings['df'] = settings['df'] if 'df' in settings else 'default'

    if settings['df'] not in dfs:
        raise Exception('Invalid df param')

    return NODES[settings['type']].run(dfs, settings)

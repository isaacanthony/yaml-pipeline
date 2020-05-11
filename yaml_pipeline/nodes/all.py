"""Run a node"""
from yaml_pipeline.nodes import \
    astype, \
    copy_dataframes, \
    download_s3, \
    drop_columns, \
    drop_dataframes, \
    drop_duplicates, \
    fillna, \
    filter_columns, \
    filter_rows, \
    groupby, \
    head, \
    merge, \
    mkdirs, \
    read_csv, \
    rename_columns, \
    rename_dataframes, \
    round as round_columns, \
    set_value, \
    to_csv

NODES = {
    'astype': astype,
    'copy_dataframes': copy_dataframes,
    'download_s3': download_s3,
    'drop_columns': drop_columns,
    'drop_dataframes': drop_dataframes,
    'drop_duplicates': drop_duplicates,
    'fillna': fillna,
    'filter_columns': filter_columns,
    'filter_rows': filter_rows,
    'groupby': groupby,
    'head': head,
    'merge': merge,
    'mkdirs': mkdirs,
    'read_csv': read_csv,
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

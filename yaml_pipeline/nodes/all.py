"""Run any possible node"""
from yaml_pipeline.nodes import \
    astype, \
    drop_columns, \
    drop_dataframes, \
    filter_columns, \
    filter_rows, \
    groupby, \
    head, \
    merge, \
    read_csv, \
    rename_columns, \
    rename_dataframes, \
    set_value, \
    to_csv

NODES = {
    'astype': astype,
    'drop_columns': drop_columns,
    'drop_dataframes': drop_dataframes,
    'filter_columns': filter_columns,
    'filter_rows': filter_rows,
    'groupby': groupby,
    'head': head,
    'merge': merge,
    'read_csv': read_csv,
    'rename_columns': rename_columns,
    'rename_dataframes': rename_dataframes,
    'set_value': set_value,
    'to_csv': to_csv,
}


def run(dfs: dict, settings: dict) -> dict:
    """Run a node"""
    settings['df'] = settings['df'] if 'df' in settings else 'default'

    if settings['df'] not in dfs:
        raise Exception('Invalid df param')

    return NODES[settings['type']].run(dfs, settings)

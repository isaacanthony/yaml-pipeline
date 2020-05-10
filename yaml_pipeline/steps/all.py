"""Run a step"""
from yaml_pipeline.steps import \
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

STEPS = {
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
    """Run a step"""
    settings['df'] = settings['df'] if 'df' in settings else 'default'

    if settings['df'] not in dfs:
        raise Exception('Invalid df param')

    return STEPS[settings['type']].run(dfs, settings)

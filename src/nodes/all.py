"""Run any possible node"""
from src.helpers import logger
from src.nodes import \
    astype, \
    drop_columns, \
    drop_dataframes, \
    filter_columns, \
    filter_rows, \
    head, \
    merge, \
    read_csv, \
    rename_columns, \
    rename_dataframes, \
    to_csv

LOG = logger.getLogger()

NODES = {
    'astype': astype,
    'drop_columns': drop_columns,
    'drop_dataframes': drop_dataframes,
    'filter_columns': filter_columns,
    'filter_rows': filter_rows,
    'head': head,
    'merge': merge,
    'read_csv': read_csv,
    'rename_columns': rename_columns,
    'rename_dataframes': rename_dataframes,
    'to_csv': to_csv,
}


def run(dfs: dict, settings: dict) -> dict:
    """Run any possible node"""
    if 'type' not in settings:
        raise Exception('Missing type param')

    if 'description' in settings:
        LOG.info("Running %s node", settings['description'])
    else:
        LOG.info("Running %s node", settings['type'])

    settings['df'] = settings['df'] if 'df' in settings else 'default'

    if settings['df'] not in dfs:
        raise Exception('Invalid df param')

    return NODES[settings['type']].run(dfs, settings)

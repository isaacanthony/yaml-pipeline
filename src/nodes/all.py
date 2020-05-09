"""Run any possible node"""
from src.helpers import logger
from src.nodes import \
    drop_columns, \
    filter_columns, \
    head, \
    read_csv, \
    rename_columns, \
    to_csv

LOG = logger.getLogger()


NODES = {
    'drop_columns': drop_columns,
    'filter_columns': filter_columns,
    'head': head,
    'read_csv': read_csv,
    'rename_columns': rename_columns,
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

    return NODES[settings['type']].run(dfs, settings)

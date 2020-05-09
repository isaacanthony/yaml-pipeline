"""Main entrypoint"""
from sys import argv
from yaml import safe_load
from src.helpers import logger
from src.nodes import all as all_nodes

LOG = logger.getLogger()


def main():
    """Main entrypoint"""
    # Check for missing params
    if len(argv) < 2:
        LOG.error('Missing pipeline parameter')
        return

    pipelines = argv[1].split(',')

    # Run pipelines
    for pipeline in pipelines:
        _run(pipeline)


def _run(pipeline: str):
    """Run pipeline"""
    LOG.info("Running %s pipeline", pipeline)

    # Import settings
    settings = safe_load(open('config/base.yml').read())
    settings.update(safe_load(open(f"config/{pipeline}.yml").read()))

    dfs = {'default': None}

    for node in settings.pop('nodes', []):
        all_nodes.run(dfs, {**settings, **node})


if __name__ == '__main__':
    main()

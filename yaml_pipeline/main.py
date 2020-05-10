"""Main entrypoint"""
from sys import argv
from yaml_pipeline import Pipelines
from yaml_pipeline.helpers import logger

LOG = logger.getLogger()


def main():
    """Main entrypoint"""
    # Check for missing params
    if len(argv) < 2:
        raise Exception('Missing pipeline parameter')

    pipelines = Pipelines(
        'config/',
        logger=LOG,
        path_prefix='data/',
    )

    # Run pipelines
    for name in argv[1].split(','):
        pipelines.run(name)


if __name__ == '__main__':
    main()

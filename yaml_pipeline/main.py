"""Main entrypoint"""
from sys import argv
import logging
from yaml_pipeline import Pipelines


def main():
    """Main entrypoint"""
    # Check for missing params
    if len(argv) < 2:
        raise Exception('Missing pipeline parameter')

    pipelines = Pipelines(
        'config/',
        logger=_get_logger(),
        path_prefix='data/',
    )

    # Run pipelines
    for name in argv[1].split(','):
        pipelines.run(name)


def _get_logger() -> logging.Logger:
    """Logging wrapper"""
    logging.basicConfig(format="%(asctime)s %(message)s")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger


if __name__ == '__main__':
    main()

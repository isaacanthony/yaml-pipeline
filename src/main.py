"""Main entrypoint"""
from sys import argv
from src.pipelines import Pipelines


def main():
    """Main entrypoint"""
    # Check for missing params
    if len(argv) < 2:
        raise Exception('Missing pipeline parameter')

    pipelines = Pipelines(
        'config/',
        logging=True,
        path_prefix='data/',
    )

    # Run pipelines
    for name in argv[1].split(','):
        pipelines.run(name)


if __name__ == '__main__':
    main()

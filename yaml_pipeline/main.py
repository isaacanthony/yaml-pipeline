"""Main entrypoint"""
from sys import argv
from yaml_pipeline import Pipeline


def main():
    """Main entrypoint"""
    # Check for missing params
    if len(argv) < 2:
        raise Exception('Missing pipeline parameter')

    pipeline = Pipeline(
        'config/',
        logging=True,
        path_prefix='data/',
    )

    # Run pipelines
    for name in argv[1].split(','):
        pipeline.run(name)


if __name__ == '__main__':
    main()

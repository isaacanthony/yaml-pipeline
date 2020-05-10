"""Pipeline wrapper"""
from yaml import safe_load
from yaml_pipeline.helpers import logger
from yaml_pipeline.steps.all import run

LOG = logger.getLogger()


class Pipeline():
    """Pipeline wrapper"""
    def __init__(self, yml_dir: str, **kwargs):  # pylint: disable=unused-argument
        self.yml_dir = yml_dir
        self.settings = locals()['kwargs']

    def run(self, name: str):
        """Run a pipeline"""
        if self.settings['logging']:
            LOG.info("Running %s pipeline", name)

        # Import settings
        pipeline = safe_load(open(f"{self.yml_dir}{name}.yml").read())
        dfs = {'default': None}

        # Run each step in pipeline
        for step in pipeline['steps']:
            if 'type' not in step:
                raise Exception('Missing type param')

            if self.settings['logging']:
                if 'description' in step:
                    LOG.info("Running %s step", step['description'])
                else:
                    LOG.info("Running %s step", step['type'])

            run(dfs, {**self.settings, **step})

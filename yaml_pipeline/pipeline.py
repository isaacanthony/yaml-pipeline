"""Pipeline wrapper"""
from yaml import safe_load
from yaml_pipeline.helpers import logger
from yaml_pipeline.nodes.all import run

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

        # Run each node in pipeline
        for node in pipeline['nodes']:
            if 'type' not in node:
                raise Exception('Missing type param')

            if self.settings['logging']:
                if 'description' in node:
                    LOG.info("Running %s node", node['description'])
                else:
                    LOG.info("Running %s node", node['type'])

            run(dfs, {**self.settings, **node})

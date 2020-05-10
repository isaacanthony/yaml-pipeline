"""Pipeline wrapper"""
from yaml_pipeline.nodes.all import run


class Pipeline():
    """Pipeline wrapper"""
    def __init__(self, dfs: dict, settings: dict):
        self.dfs = dfs
        self.settings = settings

    def run(self) -> dict:
        """Run pipeline"""
        # Run each node in pipeline
        for node in self.settings['nodes']:
            if 'type' not in node:
                raise Exception('Missing type param')

            if 'logger' in self.settings:
                if 'description' in node:
                    self.settings['logger'].info("Running %s", node['description'])
                else:
                    self.settings['logger'].info("Running %s", node['type'])

            self.dfs = run(self.dfs, {**self.settings, **node})

        return self.dfs

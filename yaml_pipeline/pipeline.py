"""Pipeline wrapper"""
from yaml_pipeline.steps.all import run


class Pipeline():
    """Pipeline wrapper"""
    def __init__(self, dfs: dict, settings: dict):
        self.dfs = dfs
        self.settings = settings

    def run(self) -> dict:
        """Run pipeline"""
        # Run each step in pipeline
        for step in self.settings['steps']:
            if 'type' not in step:
                raise Exception('Missing type param')

            if 'logger' in self.settings:
                if 'description' in step:
                    self.settings['logger'].info("Running %s step", step['description'])
                else:
                    self.settings['logger'].info("Running %s step", step['type'])

            self.dfs = run(self.dfs, {**self.settings, **step})

        return self.dfs

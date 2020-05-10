"""Pipelines wrapper"""
from yaml import safe_load
from yaml_pipeline.pipeline import Pipeline


class Pipelines():
    """Pipelines wrapper"""
    def __init__(self, yml_dir: str, **kwargs):  # pylint: disable=unused-argument
        self.yml_dir = yml_dir
        self.settings = locals()['kwargs']

    def run(self, name: str) -> dict:
        """Run a pipeline"""
        if 'logger' in self.settings:
            self.settings['logger'].info("Running %s pipeline", name)

        # Import settings
        pipeline = safe_load(open(f"{self.yml_dir}{name}.yml").read())

        # Run pipeline
        return Pipeline({**self.settings, **pipeline}).run()

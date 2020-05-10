"""Test Pipeline class"""
import unittest
import pandas as pd
from yaml_pipeline.pipeline import Pipeline

DFS = {
    'default': pd.DataFrame([{
        'id': 1,
        'name': 'Alice',
    }]),
}

SETTINGS = {
    'yaml_pipeline': [
        {
            'type': 'rename_columns',
            'columns': {
                'id': 'user_id',
            },
        },
        {
            'type': 'set_value',
            'column': 'age',
            'value': 51,
        },
    ]
}


def test_run():
    """Test pipeline.run()"""
    case = unittest.TestCase()
    pipeline = Pipeline(SETTINGS)
    pipeline.dfs = DFS
    df = pipeline.run()['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'user_id': 1,
            'name': 'Alice',
            'age': 51,
        }],
    )

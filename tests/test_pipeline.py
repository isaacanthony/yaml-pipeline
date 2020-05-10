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
    'nodes': [
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
    df = Pipeline(DFS, SETTINGS).run()['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'user_id': 1,
            'name': 'Alice',
            'age': 51,
        }],
    )

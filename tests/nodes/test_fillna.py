"""Test fillna node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

DFS = {
    'default': pd.DataFrame([{
        'id': None,
        'name': None,
    }]),
}

SETTINGS = {
    'type': 'fillna',
    'value': 0.0,
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    df = run(DFS.copy(), SETTINGS)['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'id': 0.0,
            'name': 0.0,
        }],
    )


def test_columns():
    """Test specifying columns"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'columns': ['id'],
    }

    df = run(DFS.copy(), settings)['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'id': 0.0,
            'name': None,
        }],
    )

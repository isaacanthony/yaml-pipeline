"""Test floor node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

DF = pd.DataFrame([{
    'col1': 1.68,
    'col2': 3.14,
}])


def test_floor_columns():
    """Test floor specific columns"""
    case = unittest.TestCase()

    settings = {
        'type': 'floor',
        'columns': ['col1'],
    }

    df = run({'default': DF.copy()}, settings)['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'col1': 1.0,
            'col2': 3.14,
        }],
    )


def test_floor_all():
    """Test floor all columns"""
    case = unittest.TestCase()
    df = run({'default': DF.copy()}, {'type': 'floor'})['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'col1': 1.0,
            'col2': 3.0,
        }],
    )

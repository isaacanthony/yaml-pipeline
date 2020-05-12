"""Test ceil node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

DF = pd.DataFrame([{
    'col1': 1.68,
    'col2': 3.14,
}])


def test_ceil_columns():
    """Test ceil specific columns"""
    case = unittest.TestCase()

    settings = {
        'type': 'ceil',
        'columns': ['col1'],
    }

    df = run({'default': DF.copy()}, settings)['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'col1': 2.0,
            'col2': 3.14,
        }],
    )


def test_ceil_all():
    """Test ceil all columns"""
    case = unittest.TestCase()
    df = run({'default': DF.copy()}, {'type': 'ceil'})['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'col1': 2.0,
            'col2': 4.0,
        }],
    )

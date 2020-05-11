"""Test round node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

DF = pd.DataFrame([{
    'col1': 1.68,
    'col2': 3.14,
}])


def test_round_columns():
    """Test round specific columns"""
    case = unittest.TestCase()

    settings = {
        'type': 'round',
        'columns': ['col1'],
        'decimals': 1,
    }

    df = run({'default': DF.copy()}, settings)['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'col1': 1.7,
            'col2': 3.14,
        }],
    )


def test_round_all():
    """Test round all columns"""
    case = unittest.TestCase()
    df = run({'default': DF.copy()}, {'type': 'round'})['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'col1': 2.0,
            'col2': 3.0,
        }],
    )

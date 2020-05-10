"""Test set_value step"""
import unittest
import pandas as pd
from yaml_pipeline.steps.all import run

SETTINGS = {
    'type': 'set_value',
    'column': 'id',
}


def test_static_value():
    """Test setting static value"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'value': 2,
    }

    df = run({'default': pd.DataFrame([{'id': 1}])}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'id': 2}])


def test_dynamic_value():
    """Test setting dynamic value"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'value': 'df[\'id\'] + 2',
    }

    df = run({'default': pd.DataFrame([{'id': 1}])}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'id': 3}])

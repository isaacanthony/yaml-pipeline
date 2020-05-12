"""Test assert_true node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

DF = pd.DataFrame([{
    'col1': 1,
    'col2': 1,
    'col3': 2,
}])


def test_pass():
    """Test passing assert_true statement"""
    case = unittest.TestCase()

    settings = {
        'type': 'assert',
        'value': 'df[\'col1\'].tolist() == df[\'col2\'].tolist()',
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), DF.to_dict(orient='records'))


def _failed_assertion():
    """Failing assertion lambda"""
    settings = {
        'type': 'assert',
        'value': 'df[\'col1\'].tolist() == df[\'col3\'].tolist()',
    }

    return run({'default': DF}, settings)['default']


def test_fail():
    """Test failing assert_true statement"""
    case = unittest.TestCase()
    case.assertRaises(AssertionError, _failed_assertion)

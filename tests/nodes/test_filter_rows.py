"""Test filter_rows node"""
import unittest
import pandas as pd
from src.nodes.filter_rows import run

DF = pd.DataFrame([
    {
        'id': 1,
    },
    {
        'id': 2,
    },
])

SETTINGS = {
    'type': 'filter_rows',
    'df': 'default',
}


def test_eq():
    """Test eq filter"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'column': 'id',
        'filter': 'eq',
        'value': 1,
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'id': 1}])

"""Test filter_columns node"""
import unittest
import pandas as pd
from src.nodes.filter_columns import run

DF = pd.DataFrame([{
    'col1': 1,
    'col2': 2,
    'col3': 3,
    'col4': 4,
}])

SETTINGS = {
    'type': 'filter_columns',
    'columns': [
        'col4',
        'col3',
    ],
    'df': 'default',
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    df = run({'default': DF}, SETTINGS)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'col4': 4, 'col3': 3}])

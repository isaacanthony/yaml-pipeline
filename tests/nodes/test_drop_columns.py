"""Test drop_columns node"""
import unittest
import pandas as pd
from src.nodes.drop_columns import run

DF = pd.DataFrame([{
    'col1': 1,
    'col2': 2,
    'col3': 3,
    'col4': 4,
}])

SETTINGS = {
    'type': 'drop_columns',
    'columns': [
        'col3',
        'col4',
    ],
    'df': 'default',
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    df = run({'default': DF}, SETTINGS)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'col1': 1, 'col2': 2}])

"""Test astype node"""
import unittest
import pandas as pd
from src.nodes.all import run

DF = pd.DataFrame([{'age': 51.0, 'height': '1.8'}])

SETTINGS = {
    'type': 'astype',
    'columns': {
        'age': 'int',
        'height': 'float',
    },
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    df = run({'default': DF}, SETTINGS)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'age': 51, 'height': 1.8}])

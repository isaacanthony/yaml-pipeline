"""Test drop_columns node"""
import unittest
import pandas as pd
from src.nodes.drop_columns import run

DF = pd.DataFrame(columns=['col1', 'col2', 'col3', 'col4'])

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
    dfs = run({'default': DF}, SETTINGS)
    case.assertEqual(str(list(dfs['default'])), '[\'col1\', \'col2\']')

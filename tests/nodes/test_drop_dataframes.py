"""Test drop_dataframes node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

DFS = {
    'default': None,
    'cars': pd.DataFrame([{
        'make': 'Toyota',
    }]),
}

SETTINGS = {
    'type': 'drop_dataframes',
    'dfs': ['cars'],
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    dfs = run(DFS, SETTINGS)
    case.assertEqual(list(dfs.keys()), ['default'])

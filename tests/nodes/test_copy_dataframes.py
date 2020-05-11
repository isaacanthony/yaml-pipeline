"""Test copy_dataframes node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

DFS = {
    'default': pd.DataFrame([{
        'id': 1,
        'name': 'Alice',
    }]),
}

SETTINGS = {
    'type': 'copy_dataframes',
    'dfs': {
        'default': 'users1',
        'users1': 'users2',
    },
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    dfs = run(DFS, SETTINGS)

    case.assertEqual(
        dfs['default'].to_dict(orient='records'),
        dfs['users1'].to_dict(orient='records'),
    )

    case.assertEqual(
        dfs['default'].to_dict(orient='records'),
        dfs['users2'].to_dict(orient='records'),
    )

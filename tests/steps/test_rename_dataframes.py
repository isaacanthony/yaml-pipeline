"""Test rename_dataframes step"""
import unittest
import pandas as pd
from yaml_pipeline.steps.all import run

DFS = {
    'default': None,
    'cars': pd.DataFrame([{
        'make': 'Toyota',
    }]),
    'boats': pd.DataFrame([{
        'make': 'Bayliner',
    }]),
}

SETTINGS = {
    'type': 'rename_dataframes',
    'dfs': {
        'cars': 'cars_old',
        'boats': 'boats_old',
    },
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    dfs = run(DFS, SETTINGS)
    case.assertEqual(list(dfs.keys()), ['default', 'cars_old', 'boats_old'])

    case.assertEqual(
        dfs['cars_old'].to_dict(orient='records'),
        [{
            'make': 'Toyota',
        }],
    )

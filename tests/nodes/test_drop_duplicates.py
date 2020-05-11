"""Test drop_duplicates node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

ENTRY1 = {
    'id': 1,
    'name': 'Alice',
}

ENTRY2 = {
    'id': 2,
    'name': 'Alice',
}

DFS = {
    'default': pd.DataFrame([ENTRY1, ENTRY1, ENTRY2]),
}

SETTINGS = {
    'type': 'drop_duplicates',
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    df = run(DFS.copy(), SETTINGS)['default']
    case.assertEqual(df.to_dict(orient='records'), [ENTRY1, ENTRY2])


def test_subset():
    """Test specifying subset"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'subset': ['name'],
    }

    df = run(DFS.copy(), settings)['default']
    case.assertEqual(df.to_dict(orient='records'), [ENTRY1])


def test_keep():
    """Test specifying keep"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'subset': ['name'],
        'keep': 'last',
    }

    df = run(DFS.copy(), settings)['default']
    case.assertEqual(df.to_dict(orient='records'), [ENTRY2])

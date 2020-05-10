"""Test merge node"""
import unittest
import pandas as pd
from yaml_pipeline.nodes.all import run

DF1 = pd.DataFrame([{
    'id': 1,
    'name': 'Alice',
}])

DF2 = pd.DataFrame([{
    'id': 1,
    'age': 51,
}])

DFS = {
    'default': None,
    'names': DF1,
    'ages': DF2,
}

SETTINGS = {
    'type': 'merge',
    'dfs': [
        'names',
        'ages',
    ],
}


def test_inner():
    """Test inner merge"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'on': 'id',
    }

    df = run(DFS, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'id': 1, 'name': 'Alice', 'age': 51}])


def test_left():
    """Test left merge"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'how': 'left',
        'on': ['id'],
    }

    df = run(DFS, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'id': 1, 'name': 'Alice', 'age': 51}])


def test_left_on_right_on():
    """Test left_on, right_on merge"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'left_on': ['id'],
        'right_on': ['id'],
    }

    df = run(DFS, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'id': 1, 'name': 'Alice', 'age': 51}])

"""Test filter_rows node"""
import unittest
import pandas as pd
import numpy as np
from yaml_pipeline.nodes.all import run

ALICE = [{'id': 1, 'name': 'Alice'}]
BOB = [{'id': 2, 'name': 'Bob'}]
CHARLIE = [{'id': np.nan, 'name': 'Charlie'}]
DF = pd.DataFrame(ALICE + BOB)


def test_contains():
    """Test contains filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'name',
        'filter': 'contains',
        'value': '[Ll]ice',
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), ALICE)


def test_endswith():
    """Test endswith filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'name',
        'filter': 'endswith',
        'value': 'e',
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), ALICE)


def test_eq():
    """Test eq filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'eq',
        'value': 2,
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), BOB)


def test_gt():
    """Test gt filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'gt',
        'value': 1,
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), BOB)


def test_gte():
    """Test gte filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'gte',
        'value': 2,
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), BOB)


def test_in():
    """Test in filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'in',
        'value': [1, 3],
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), ALICE)


def test_lt():
    """Test lt filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'lt',
        'value': 2,
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), ALICE)


def test_lte():
    """Test lte filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'lte',
        'value': 1,
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), ALICE)


def test_null():
    """Test null filter"""
    case = unittest.TestCase()
    df = pd.DataFrame(ALICE + CHARLIE)

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'null',
    }

    df = run({'default': df}, settings)['default']
    case.assertEqual(str(df.to_dict(orient='records')), str(CHARLIE))


def test_startswith():
    """Test startswith filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'name',
        'filter': 'startswith',
        'value': 'A',
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), ALICE)


def test_not_contains():
    """Test not.contains filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'name',
        'filter': 'not.contains',
        'value': '[Oo]',
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), ALICE)


def test_not_endswith():
    """Test not.endswith filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'name',
        'filter': 'not.endswith',
        'value': 'e',
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), BOB)


def test_not_eq():
    """Test not.eq filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'name',
        'filter': 'not.eq',
        'value': 'Alice',
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), BOB)


def test_not_in():
    """Test not.in filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'not.in',
        'value': [1, 3],
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), BOB)


def test_not_null():
    """Test not.null filter"""
    case = unittest.TestCase()
    df = pd.DataFrame(ALICE + CHARLIE)

    settings = {
        'type': 'filter_rows',
        'column': 'id',
        'filter': 'not.null',
    }

    df = run({'default': df}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), ALICE)


def test_not_startswith():
    """Test not.startswith filter"""
    case = unittest.TestCase()

    settings = {
        'type': 'filter_rows',
        'column': 'name',
        'filter': 'not.startswith',
        'value': 'Al',
    }

    df = run({'default': DF}, settings)['default']
    case.assertEqual(df.to_dict(orient='records'), BOB)

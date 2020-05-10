"""Test groupby step"""
import unittest
import pandas as pd
from yaml_pipeline.steps.all import run

DF = pd.DataFrame([
    {
        'id': 1,
        'country': 'USA',
        'age': 51,
    },
    {
        'id': 2,
        'country': 'USA',
        'age': 49,
    },
])

SETTINGS = {
    'type': 'groupby',
    'by': 'country',
}


def test_overall_groupby():
    """Test overall groupby"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'agg': 'mean',
    }

    df = run({'default': DF}, settings)['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'country': 'USA',
            'id': 1.5,
            'age': 50.0,
        }],
    )


def test_column_by_column_groupby():
    """Test column-by-column groupby"""
    case = unittest.TestCase()

    settings = {
        **SETTINGS,
        'agg': {
            'id': 'count',
            'age': 'sum',
        },
    }

    df = run({'default': DF}, settings)['default']

    case.assertEqual(
        df.to_dict(orient='records'),
        [{
            'country': 'USA',
            'id': 2,
            'age': 100,
        }],
    )

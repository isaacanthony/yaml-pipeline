"""Test rename_columns step"""
import unittest
import pandas as pd
from yaml_pipeline.steps.all import run

DF = pd.DataFrame([{
    'col1': 1,
    'col2': 2,
}])

SETTINGS = {
    'type': 'rename_columns',
    'columns': {
        'col1': 'col0',
    },
}


def test_run():
    """Test run()"""
    case = unittest.TestCase()
    df = run({'default': DF}, SETTINGS)['default']
    case.assertEqual(df.to_dict(orient='records'), [{'col0': 1, 'col2': 2}])

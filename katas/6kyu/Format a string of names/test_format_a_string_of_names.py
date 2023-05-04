import importlib
from asserts.asserts import assert_true

namelist = importlib.import_module('katas.6kyu.Format a string of names.solution').namelist


class TestSolution:
    def test_format_a_string_of_names(self):
        assert_true(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]), 'Bart, Lisa & Maggie')
        assert_true(namelist([{'name': 'Bart'}]), 'Bart')

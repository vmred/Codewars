import importlib
from asserts.asserts import assert_true

parts_sums = importlib.import_module('katas.6kyu.Sum of parts.solution').parts_sums


class TestSolution:
    def test_sum_of_parts(self):
        assert_true(parts_sums([]), [0])
        assert_true(parts_sums([0, 1, 3, 6, 10]), [20, 20, 19, 16, 10, 0])

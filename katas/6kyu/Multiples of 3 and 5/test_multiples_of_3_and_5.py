import importlib
from asserts.asserts import assert_true

solution = importlib.import_module('katas.6kyu.Multiples of 3 and 5.solution').solution


class TestSolution:
    def test_multiples_of_3_and_5(self):
        assert_true(solution(10), 23)

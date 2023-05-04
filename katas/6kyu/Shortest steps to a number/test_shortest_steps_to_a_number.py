import importlib
from asserts.asserts import assert_true

shortest_steps_to_num = importlib.import_module('katas.6kyu.Shortest steps to a number.solution').shortest_steps_to_num


class TestSolution:
    def test_shortest_steps_to_a_number(self):
        assert_true(shortest_steps_to_num(16), 4)
        assert_true(shortest_steps_to_num(71), 9)

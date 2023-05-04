import importlib
from asserts.asserts import assert_true

List = importlib.import_module('katas.7kyu.Remove all the marked elements of a list.solution').List


class TestSolution:
    def test_remove_all_marked_from_list(self):
        l = List()
        assert_true(l.remove_([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]), [2, 2, 4])

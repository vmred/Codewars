from asserts.asserts import assert_true
import importlib

length = importlib.import_module('katas.kyu7.Fun with lists - length.solution').length
Node = importlib.import_module('katas.kyu7.Fun with lists - length.solution').Node


class TestSolution:
    def test_fun_with_lists_length(self):
        head = None
        assert_true(length(head), 0)

        n1 = Node(1)
        n2 = Node(2, n1)
        n3 = Node(3, n2)
        head = Node(4, n3)
        assert_true(length(head), 4)
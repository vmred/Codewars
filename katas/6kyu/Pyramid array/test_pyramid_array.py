import importlib
from asserts.asserts import assert_true

pyramid = importlib.import_module('katas.6kyu.Pyramid array.solution').pyramid


class TestSolution:
    def test_pyramid_array(self):
        assert_true(pyramid(0), [])
        assert_true(pyramid(1), [[1]])
        assert_true(pyramid(2), [[1], [1, 1]])
        assert_true(pyramid(3), [[1], [1, 1], [1, 1, 1]])

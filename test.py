import sort
import unittest

class SortTestFunctions(unittest.TestCase):
    def setUp(self):
        self.ranges = [
            [],
            [1],
            [3, 2, 5, 2, 3, 7, 4, 7],
            [1, 1, 1, 1],
            [1, 1, 1, 2],
            [2, 1, 1, 1],
            [1, 2, 1, 2],
            [4, 3, 2, 1],
        ]

    def _isSorted(self, sequence):
        prev = None
        for item in sequence:
            if item < prev:
                return False
            prev = item
        return True

    def _test_sort(self, sort_func_name):
        sort_func = getattr(sort, sort_func_name)
        for range in self.ranges:
            sort_func(range)
            self.assertTrue(self._isSorted(range))
        self.assertRaises(TypeError, sort_func, (1, 2, 3))
        self.assertRaises(TypeError, sort_func, 'hello')

    def test_bubble_sort(self):
        self._test_sort('bubble_sort')

    def test_selection_sort(self):
        self._test_sort('selection_sort')

    def test_coctail_sort(self):
        self._test_sort('coctail_sort')

if __name__ == '__main__':
    unittest.main()

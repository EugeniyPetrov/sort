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
            [4, 3, 2, 1]
        ]

    def _isSorted(self, sequence):
        prev = None
        for item in sequence:
            if item < prev:
                return False
            prev = item
        return True

    @staticmethod
    def compareTupples(a, b):
        if a[0] == b[0]:
            return 0
        return -1 if a[0] < b[0] else 1

    def _test_sort(self, sort_func_name, *args):
        sort_func = getattr(sort, sort_func_name)
        for range in self.ranges:
            sort_func(range, None, *args)
            self.assertTrue(self._isSorted(range))
        self.assertRaises(TypeError, sort_func, (1, 2, 3), None, *args)
        self.assertRaises(TypeError, sort_func, 'hello', None, *args)
        self.assertRaises(TypeError, sort_func, [1, 2, 3], 'some_func', *args)

        # Check for stability for sorted arrays
        sorted_ranges = [
            [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5)],
            [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)],
        ]
        for sorted_range in sorted_ranges:
            sort_func(sorted_range, self.compareTupples, *args)
            for i in xrange(len(sorted_range)):
                self.assertTrue(i == sorted_range[i][1])

    def test_bubble_sort(self):
        self._test_sort('bubble_sort')

    def test_selection_sort(self):
        self._test_sort('selection_sort')

    def test_coctail_sort(self):
        self._test_sort('coctail_sort')

    def test_insertion_sort(self):
        self._test_sort('insertion_sort')

    def test_shell_sort(self):
        self._test_sort('shell_sort')

    def test_shell_sort_shell_gap(self):
        self._test_sort('shell_sort', 'shell')

    def test_shell_sort_cuira_gap(self):
        self._test_sort('shell_sort', 'cuira')

    def test_comb_sort(self):
        self._test_sort('comb_sort')

if __name__ == '__main__':
    unittest.main()

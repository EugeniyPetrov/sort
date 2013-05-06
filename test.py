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

    def test_bubble_sort(self):
        for range in self.ranges:
            sort.bubble_sort(range)
            self.assertTrue(self._isSorted(range))

    def test_selection_sort(self):
        for range in self.ranges:
            sort.selection_sort(range)
            self.assertTrue(self._isSorted(range))

if __name__ == '__main__':
    unittest.main()

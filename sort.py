"""Implementation of sorting algorithms

Functions:
selection_sort(a, compare) -- in-place comparsion sort.
    """

def selection_sort(a, compare):
    """Selection sort implementation

    Time complexity - O(n^2).
    The algorithm divides the input list into two parts: the sublist of items
    already sorted, which is built up from left to right at the front (left) of
    the list, and the sublist of items remaining to be sorted that occupy the
    rest of the list. Initially, the sorted sublist is empty and the unsorted
    sublist is the entire input list. The algorithm proceeds by finding the
    smallest (or largest, depending on sorting order) element in the unsorted
    sublist, exchanging it with the leftmost unsorted element (putting it in
    sorted order), and moving the sublist boundaries one element to the right.
    (http://en.wikipedia.org/wiki/Selection_sort)"""
    for position in xrange(len(a) - 1):
        min = position
        for tail in xrange(position + 1, len(a)):
            if compare(a[tail], a[min]):
                min = tail
        if position != min:
            a[position], a[min] = a[min], a[position]

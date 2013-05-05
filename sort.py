"""Implementation of sorting algorithms

Functions:

selection_sort -- in-place comparsion sort. Time complexity - O(n^2). (http://en.wikipedia.org/wiki/Selection_sort)"""

def selection_sort(a, compare):
    """Selection sort implementation"""
    for position in xrange(len(a) - 1):
        min = position
        for tail in xrange(position + 1, len(a)):
            if compare(a[tail], a[min]):
                min = tail
        if position != min:
            a[position], a[min] = a[min], a[position]

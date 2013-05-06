"""Implementation of sorting algorithms

Functions:
selection_sort(a, compare) - in-place comparsion sort."""

def selection_sort(a, compare):
    """Selection sort implementation
    
        a - source array to be sorted
        compare - compare function. compare(a, b) -> true. Must returns true
            if a < b and false in other cases.
    
        The algorithm divides the input list into two parts: the sublist of items
        already sorted, which is built up from left to right at the front (left) of
        the list, and the sublist of items remaining to be sorted that occupy the
        rest of the list. Initially, the sorted sublist is empty and the unsorted
        sublist is the entire input list. The algorithm proceeds by finding the
        smallest (or largest, depending on sorting order) element in the unsorted
        sublist, exchanging it with the leftmost unsorted element (putting it in
        sorted order), and moving the sublist boundaries one element to the right.
        Worst case perfomance - O(n^2)
        Best case perfomance - O(n^2)
        Average case perfomance - O(n^2)
        Worst case space complexity - O(n) total, O(1) auxiliary
        (http://en.wikipedia.org/wiki/Selection_sort)"""
    for position in xrange(len(a) - 1):
        min = position
        for tail in xrange(position + 1, len(a)):
            if compare(a[tail], a[min]):
                min = tail

        if position != min:
            (a[position], a[min],) = (a[min], a[position])




def buble_sort(a, compare):
    """Buble sort implementation
    
        a - source array to be sorted
        compare - compare function. compare(a, b) -> true. Must returns true
            if a < b and false in other cases.
    
        works by repeatedly stepping through the list to be sorted, comparing each
        pair of adjacent items and swapping them if they are in the wrong order.
        The pass through the list is repeated until no swaps are needed, which
        indicates that the list is sorted.
        Worst case perfomance - O(n^2)
        Best case perfomance - O(n)
        Average case perfomance - O(n^2)
        Worst case space complexity - O(1) auxiliary
        (http://en.wikipedia.org/wiki/Bubble_sort)"""
    unsorted_head = len(a)
    while unsorted_head != 0:
        last_swap_position = 0
        for position in xrange(unsorted_head - 1):
            if compare(a[(position + 1)], a[position]):
                (a[position + 1], a[position],) = (a[position], a[(position + 1)])
                last_swap_position = position + 1

        unsorted_head = last_swap_position

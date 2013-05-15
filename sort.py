"""Implementation of sorting algorithms

Functions:
selection_sort(collection, compare) - in-place comparsion sort."""

def compare(a, b):
    if a == b:
        return 0
    else:
        return -1 if a < b else 1

def selection_sort(collection, compare_func=None):
    """Selection sort implementation
    
        collection - source list to be sorted
        compare_func - compare function. compare(a, b) -> int. Must return value
            less, greater or equal to 0 if a < b, a > b or a == b respectively
    
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

    if not isinstance(collection, list):
        raise TypeError('collection is not instance of list')

    if compare_func is None:
        compare_func = compare

    for position in xrange(len(collection) - 1):
        min = position
        for tail in xrange(position + 1, len(collection)):
            if compare_func(collection[tail], collection[min]) < 0:
                min = tail

        if position != min:
            collection[position], collection[min] = collection[min], collection[position]

def bubble_sort(collection, compare_func=None):
    """Bubble sort implementation
    
        collection - source list to be sorted
        compare_func - compare function. compare(a, b) -> int. Must return value
            less, greater or equal to 0 if a < b, a > b or a == b respectively
    
        works by repeatedly stepping through the list to be sorted, comparing each
        pair of adjacent items and swapping them if they are in the wrong order.
        The pass through the list is repeated until no swaps are needed, which
        indicates that the list is sorted.
        Worst case perfomance - O(n^2)
        Best case perfomance - O(n)
        Average case perfomance - O(n^2)
        Worst case space complexity - O(1) auxiliary
        (http://en.wikipedia.org/wiki/Bubble_sort)"""

    if not isinstance(collection, list):
        raise TypeError('collection is not instance of list')

    if compare_func is None:
        compare_func = compare

    unsorted_head = len(collection)
    while unsorted_head != 0:
        last_swap_position = 0
        for position in xrange(unsorted_head - 1):
            if compare_func(collection[position + 1], collection[position]) < 0:
                collection[position + 1], collection[position] = collection[position], collection[position + 1]
                last_swap_position = position + 1

        unsorted_head = last_swap_position

def coctail_sort(collection, compare_func=None):
    """Coctail sort implementation

        collection - source list to be sorted
        compare_func - compare function. compare(a, b) -> int. Must return value
            less, greater or equal to 0 if a < b, a > b or a == b respectively.

        Cocktail sort is a slight variation of bubble sort. It differs in that
        instead of repeatedly passing through the list from bottom to top, it
        passes alternately from bottom to top and then from top to bottom. It
        can achieve slightly better performance than a standard bubble sort.
        Worst case perfomance - O(n^2)
        Best case perfomance - O(n)
        Average case perfomance - O(n^2)
        Worst case space complexity - O(1)
        (http://en.wikipedia.org/wiki/Cocktail_sort)"""

    if not isinstance(collection, list):
        raise TypeError('collection is not instance of list')

    if compare_func is None:
        compare_func = compare

    start = 0
    end = len(collection) - 1

    swaps = True
    while swaps:
        swaps = False
        for position in xrange(start, end):
            if compare_func(collection[position + 1], collection[position]) < 0:
                collection[position + 1], collection[position] = collection[position], collection[position + 1]
                swaps = True
                end = position
        if swaps:
            swaps = False
            for position in xrange(end, start, -1):
                if compare_func(collection[position], collection[position - 1]) < 0:
                    collection[position], collection[position - 1] = collection[position - 1], collection[position]
                    swaps = True
                    start = position

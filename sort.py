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

def insertion_sort(collection, compare_func=None):
    """Insertion sort implementation

        collection - source list to be sorted
        compare_func - compare function. compare(a, b) -> int. Must return value
            less, greater or equal to 0 if a < b, a > b or a == b respectively.

        Insertion sort iterates, consuming one input element each repetition, and
        growing a sorted output list. On a repetition, insertion sort removes one
        element from the input data, finds the location it belongs within the sorted
        list, and inserts it there. It repeats until no input elements remain.
        Worst case perfomance - O(n^2) comparisons, swaps
        Best case perfomance - O(n) comparisons, O(1) swaps
        Average case perfomance - O(n^2) comparisons, swaps
        Worst case space complexity - O(n) total, O(1) auxiary
        (http://en.wikipedia.org/wiki/Insertion_sort)"""

    if not isinstance(collection, list):
        raise TypeError('collection is not instance of list')

    if compare_func is None:
        compare_func = compare

    for index_to_rearange in xrange(1, len(collection)):
        if compare_func(collection[index_to_rearange], collection[index_to_rearange - 1]) < 0:
            value_to_rearange = collection[index_to_rearange]
            hole_index = index_to_rearange
            while compare_func(value_to_rearange, collection[hole_index - 1]) < 0 and hole_index > 0:
                collection[hole_index] = collection[hole_index - 1]
                hole_index -= 1
            collection[hole_index] = value_to_rearange

def _shell_gap_sequence(collection_length):
    if collection_length > 0:
        gap, k = None, 0
        while gap != 1:
            gap = collection_length / 2 ** k
            yield gap
            k += 1

def shell_sort(collection, compare_func=None, gap_sequence=None):
    """Shell sort implementation

        collection - source list to be sorted
        compare_func - compare function. compare(a, b) -> int. Must return value
            less, greater or equal to 0 if a < b, a > b or a == b respectively.
        gap_sequence - gap sequence method. One of:
            shell - N/2^k, worst-case time complexity - O(N^2), when N=2^p
            frank_lazarus - 2(N/2^(k+1))+1, worst-case time complexity - O(N^(3/2))
            hibbard - 2^k-1, worst-case time complexity - O(N^(3/2))
            papernov_stasevich - 2^k+1, worst-case time complexity - O(N^(3/2))
            pratt - 2^p*3^q, worst-case time complexity - O(N*(log^2(N)))
            knuth - (3^k-1)/2, worst-case time complexity - O(N^(3/2))
            incerpi_sedgewick -,
            sedgewick - 4^k+3*2^(k-1)+1, worst-case time complexity - O(N^(4/3))
            sedgewick2 - 9*(4^(k-1)-2^(k-1)) + 1.4^(k+1)-6*2^k+1, worst-case time
                complexity - O(N^(4/3))
            gonnet_baeza_yatez -,
            tokuda - (9^k-4^k)/(5*4^(k-1)),
            cuira - [701, 301, 132, 57, 23, 10, 4, 1]
        by default cuira gap sequence is used as it is most effective for array
            with size up to 4000 elements

        Shellsort is a multi-pass algorithm. Each pass is an insertion sort of the
            sequences consisting of every h-th element for a fixed gap h (also known
            as the increment). This is referred to as h-sorting.
        Worst-case space complexity O(n) total, O(1) auxilary
        (http://en.wikipedia.org/wiki/Shellsort)"""

    if not isinstance(collection, list):
        raise TypeError('collection is not instance of list')

    if compare_func is None:
        compare_func = compare

    if gap_sequence is None:
        gap_sequence = 'cuira'

    collection_len = len(collection)

    if gap_sequence is 'cuira':
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    elif gap_sequence is 'shell':
        gaps = _shell_gap_sequence(collection_len)
    elif gap_sequence in ('frank_lazarus', 'hibbard', 'papernov_stasevich', 'pratt',
        'knuth', 'incerpi_sedgewick', 'sedgewick', 'sedgewick2', 'gonnet_baeza_yatez', 'tokuda'):
        raise NotImplementedError('Method not implemented yet')
    else:
        raise ValueError('Invaid gap sequence method')

    for gap in gaps:
        for sub_sequence_start in xrange(0, gap):
            for index_to_rearange in xrange(sub_sequence_start + gap, collection_len, gap):
                if compare_func(collection[index_to_rearange], collection[index_to_rearange - gap]) < 0:
                    value_to_rearange = collection[index_to_rearange]
                    hole_index = index_to_rearange
                    while compare_func(value_to_rearange, collection[hole_index - gap]) < 0 and hole_index > sub_sequence_start:
                        collection[hole_index] = collection[hole_index - gap]
                        hole_index -= gap
                    collection[hole_index] = value_to_rearange


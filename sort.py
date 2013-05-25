"""Implementation of sorting algorithms

Functions:
selection_sort(collection, compare) - in-place comparsion sort."""

def compare(a, b):
    """Default compare method for integer items.

    Compare integer a and b and return integer value less, greater or equal to 0
    if a < b, a > b or a == b respectively"""

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

    sorted = False
    while not sorted:
        sorted = True
        for position in xrange(start, end):
            if compare_func(collection[position + 1], collection[position]) < 0:
                collection[position + 1], collection[position] = collection[position], collection[position + 1]
                sorted = False
                end = position
        if not sorted:
            sorted = True
            for position in xrange(end, start, -1):
                if compare_func(collection[position], collection[position - 1]) < 0:
                    collection[position], collection[position - 1] = collection[position - 1], collection[position]
                    sorted = False
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

def comb_sort(collection, compare_func=None):
    """Comb sort implementation

        collection - source list to be sorted
        compare_func - compare function. compare(a, b) -> int. Must return value
            less, greater or equal to 0 if a < b, a > b or a == b respectively.

        Comb sort improves on bubble sort. In bubble sort, when any two elements
        are compared, they always have a gap (distance from each other) of 1.
        The basic idea of comb sort is that the gap can be much more than 1.
        The gap starts out as the length of the list being sorted divided by
        the shrink factor (generally 1.3), and the list is sorted with that value
        (rounded down to an integer if needed) as the gap. Then the gap is divided
        by the shrink factor again, the list is sorted with this new gap, and the
        process repeats until the gap is 1. At this point, comb sort continues
        using a gap of 1 until the list is fully sorted. The final stage of the
        sort is thus equivalent to a bubble sort, but by this time most turtles
        have been dealt with, so a bubble sort will be efficient.
        (http://en.wikipedia.org/wiki/Comb_sort)"""

    if not isinstance(collection, list):
        raise TypeError('collection is not instance of list')

    if compare_func is None:
        compare_func = compare

    collection_len = len(collection)
    gap = collection_len
    shrink_factor = 1.3
    sorted = False

    while not sorted or gap is not 1:
        sorted = True
        gap = int(gap / shrink_factor)
        if gap < 1:
            gap = 1

        for sub_sequence_start in xrange(0, gap):
            for position in xrange(sub_sequence_start + gap, collection_len, gap):
                if compare_func(collection[position], collection[position - gap]) < 0:
                    collection[position], collection[position - gap] = collection[position - gap], collection[position]
                    sorted = False

def _merge(collection, buffer, left_seq, right_seq, compare_func):
    """Merge 2 sub-sequences from collection specified by left_seq and right_seq and put them to the buffer
        list at the same positions.

        left_seq and right_seq are tuples like (from, to)
        collection - list of sub-sequences
        buffer - list to be populated by merge result
        compare_func - function to compare items at the begining of sub-sequences

        Merge is done by getting the first elements of both sub-sequences, compare them with compare_func and
        produce new sequence with less elements. Thereby if sub-sequences are sorted then produced by merge list
        will also be sorted.
        Used by merge sort algorithm."""

    left_from, left_to = left_seq[0], left_seq[1]
    right_from, right_to = right_seq[0], right_seq[1]

    if not isinstance(collection, list) or not isinstance(buffer, list):
        raise TypeError('collection and buffer must be an instances of list')

    if not isinstance(left_seq, tuple) or not isinstance(right_seq, tuple):
        raise TypeError('left_seq and right_seq must be an instances of tuple')

    if left_from < 0 or right_from < 0 or left_to >= len(collection) or right_to >= len(collection):
        raise ValueError('sub-sequences must be inside of collection')

    if right_from - left_to != 1:
        raise ValueError('right_seq must be right after left_seq')

    if left_to < left_from or right_to < right_from:
        raise ValueError('Invalid sub-sequences')

    if len(collection) != len(buffer):
        raise ValueError('both colleciton and buffer must me the same length')

    for i in xrange(left_from, right_to + 1):
        next_item = None
        if left_from > left_to:
            next_item = right_from
            right_from += 1
        elif right_from > right_to:
            next_item = left_from
            left_from += 1

        if next_item is None:
            if compare_func(collection[right_from], collection[left_from]) < 0:
                next_item = right_from
                right_from += 1
            else:
                next_item = left_from
                left_from += 1

        buffer[i] = collection[next_item]

def _get_sorted_sequences(collection, compare_func):
    """Sorted sub-sequences generator

        Find sorted sub-sequences on collection and generates a tuples with positions
        of sub-sequences in (from, to) format"""
    if not isinstance(collection, list):
        raise TypeError('collection is not instance of list')

    collection_len = len(collection)
    if collection_len > 0:
        seq_start = 0
        for i in xrange(1, collection_len):
            if compare_func(collection[i], collection[i - 1]) < 0:
                yield (seq_start, i - 1)
                seq_start = i
        yield (seq_start, collection_len - 1)

def merge_sort(collection, compare_func=None):
    """Natutal merge sort implementation

        collection - source list to be sorted
        compare_func - compare function. compare(a, b) -> int. Must return value
            less, greater or equal to 0 if a < b, a > b or a == b respectively.

        Algorithm is done by divide the unsorted list into N sorted subslists, and
        then repeatedly merge them to produce new sorted sublists until only 1
        sublist remaining. This will be the sorted list.
        Worst case performance - O(n log n)
        Best case performance - O(n)
        Average case performance - O(n log n)
        Worst case space complexity - O(n) auxilary
        (http://en.wikipedia.org/wiki/Merge_sort)"""

    if not isinstance(collection, list):
        raise TypeError('collection is not instance of list')

    if compare_func is None:
        compare_func = compare

    work = collection
    buffer = None

    is_sorted = False
    while not is_sorted:
        first_seq = None
        sequences_count = 0
        for seq in _get_sorted_sequences(work, compare_func):
            if first_seq is None:
                first_seq = seq
            else:
                # allocate memory for buffer only before merge. (no merge needed if already sorted)
                if buffer is None:
                    buffer = [None] * len(collection)
                _merge(work, buffer, first_seq, seq, compare_func)
                first_seq = None

            sequences_count += 1

        if sequences_count > 1 and sequences_count % 2 == 1:
            buffer[first_seq[0]:first_seq[1] + 1] = collection[first_seq[0]:first_seq[1] + 1]

        if sequences_count <= 2:
            is_sorted = True
        else:
            work, buffer = buffer, work

    if buffer is not None and buffer is not collection:
        collection[:] = buffer[:]

import sort
import random
import time
import csv
import argparse

with open('perfomance.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Algorithm', 'Range size', 'Random', 'Sorted', 'Nearly sorted', 'Reversed', 'Few unique'])

    for sort_name in ['comb_sort', 'shell_sort', 'insertion_sort']:
	sort_func = getattr(sort, sort_name)
        for range_size in xrange(100, 10000, 100):
            random_list = [i for i in random.sample(xrange(0, 1000000000), range_size)]
            sorted = [i for i in xrange(0, range_size)]
            nearly_sorted = [i + random.randrange(-int(range_size * 0.2), int(range_size * 0.2)) for i in xrange(range_size)]
            reversed = [i for i in xrange(range_size, 0)]
            few_unique = [i % 10 for i in random.sample(xrange(0, 1000000000), range_size)]

            range = random_list[:]
            start = time.time()
            sort_func(range)
            random_exec_time = time.time() - start

            range = sorted[:]
            start = time.time()
            sort_func(range)
            sorted_exec_time = time.time() - start

            range = nearly_sorted[:]
            start = time.time()
            sort_func(range)
            nearly_sorted_exec_time = time.time() - start

            range = reversed[:]
            start = time.time()
            sort_func(range)
            reversed_exec_time = time.time() - start

            range = few_unique[:]
            start = time.time()
            sort_func(range)
            few_unique_exec_time = time.time() - start

            csvwriter.writerow([sort_name, range_size, random_exec_time, sorted_exec_time, nearly_sorted_exec_time, reversed_exec_time, few_unique_exec_time])
            print "range of size {0} done for {1}".format(range_size, sort_name)

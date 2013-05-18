import sort

a = [71, 49, 69, 46, 43, 3, 73, 38, 77, 16, 65, 79, 80, 24, 2, 31, 55, 1, 82, 64]

b = a[:]
sort.shell_sort(b)
print b

b = a[:]
sort.shell_sort(b, None, 'shell')
print b

b = a[:]
sort.shell_sort(b, None, 'cuira')
print b

b = a[:]
sort.insertion_sort(b)
print b

b = a[:]
sort.coctail_sort(b)
print b

b = a[:]
sort.selection_sort(b)
print b

b = a[:]
sort.bubble_sort(b)
print b

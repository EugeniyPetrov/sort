import sort

a = [71, 49, 69, 46, 43, 3, 73, 38, 77, 16, 65, 79, 80, 24, 2, 31, 55, 1, 82, 64]

def compare (a, b):
    return a < b

sort.selection_sort(a, compare)
print a

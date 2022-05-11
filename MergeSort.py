def merge_sort(array):
    if len(array) <= 1:
        return

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_list(left, right, array)


def merge_sorted_list(a, b, array):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1
        else:
            array[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        array[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        array[k] = b[j]
        j += 1
        k += 1


array = [10, 3, 15, 7, 8, 23, 98, 29]
merge_sort(array)
print(array)

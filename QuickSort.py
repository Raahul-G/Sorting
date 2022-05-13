def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(ele, start, end):
    if start < end:
        pi = partition(ele, start, end)
        quick_sort(ele, start, pi - 1)  # left
        quick_sort(ele, pi + 1, end)  # right


array = [11, 9, 29, 7, 2, 15, 28]
quick_sort(array, 0, len(array) - 1)
print(array)

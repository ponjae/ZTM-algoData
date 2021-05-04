def quick_sort(arr, left, right):
    pivot = None
    partion_index = None
    if left < right:
        pivot = right
        partion_index = partion(arr, pivot, left, right)

        quick_sort(arr, left, partion_index - 1)
        quick_sort(arr, partion_index + 1, right)
    return arr


def partion(arr, pivot, left, right):
    pivot_value = arr[pivot]
    partion_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, partion_index)
            partion_index += 1
    swap(arr, right, partion_index)
    return partion_index


def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(numbers, 0, len(numbers)-1))

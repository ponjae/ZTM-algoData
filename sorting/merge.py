def merge_sort(arr):
    length = len(arr)
    if len(arr) == 1:
        return arr
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result + left[left_index:] + right[right_index:]


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(merge_sort(numbers))

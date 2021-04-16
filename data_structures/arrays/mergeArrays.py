# given two sorted array, create a function that merges these two to one sorted array
# mergeSoryedArrays([0,3,4,31], [4,5,30]) --> [0, 3, 4, 4, 6, 30, 31]
# This solution should have O(n) time-complexity

def merge_sorted_arrays(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2

    merged_list = []
    arr1_index = 0
    arr2_index = 0

    while arr1_index < len(arr1) and arr2_index < len(arr2):
        arr1_elem = arr1[arr1_index]
        arr2_elem = arr2[arr2_index]
        if arr1_elem < arr2_elem:
            merged_list.append(arr1_elem)
            arr1_index += 1
        else:
            merged_list.append(arr2_elem)
            arr2_index += 1

    return merged_list + arr1[arr1_index:] + arr2[arr2_index:]


print(merge_sorted_arrays([0, 3, 4, 31], [4, 5, 30]))

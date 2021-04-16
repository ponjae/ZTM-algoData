'''
Find the first recurring character in a given array!

Given an array = [2,5,1,2,3,5,1,2,4]
Should return 2

Given an array = [2,1,1,2,3,5,1,2,4]
Should return 1

Given an array = [2,3,4,5]
Should return undefined
'''


def brute_force_approach(array):  # O(n^2)
    min_rec_index = len(array) + 1
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                if j < min_rec_index:
                    min_rec_index = j
    if min_rec_index <= len(array):
        return array[min_rec_index]
    else:
        return None


print(brute_force_approach([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(brute_force_approach([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(brute_force_approach([2, 3, 4, 5]))
print(brute_force_approach([]))
print(brute_force_approach([2, 3, 4, 5, 6, 7, 8, 1, 8, 1]))


def linear_approach(array):  # O(n)
    hashmap = {}
    for item in array:
        if hashmap.get(item) is not None:
            return item
        hashmap[item] = True
    return None


print(linear_approach([2, 5, 1, 2, 3, 5, 1, 2, 4]), 'linear')
print(linear_approach([2, 1, 1, 2, 3, 5, 1, 2, 4]), 'linear')
print(linear_approach([2, 3, 4, 5]), 'linear')
print(linear_approach([]), 'linear')

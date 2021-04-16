# with a given array and a given number, see if there are elements in the array that sums up to the number given
import time


def brute_force_approach(li, nbr):
    t1 = time.time()
    found = False
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[i] + li[j+1] == nbr:
                found = True
                break
    if found:
        print(f'Pair available')
    else:
        print('No elements in list available')
    t2 = time.time()
    print(t2 - t1, ' brute')


# brute_force_approach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
#                      13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 35, 36], 33)


def linear_approach(li, nbr):
    t1 = time.time()
    first = 0
    last = len(li) - 1
    found = False
    while last > first:
        added = li[first] + li[last]
        if added == nbr:
            found = True
            break
        elif added > nbr:
            last -= 1
        else:
            first += 1
    if found:
        print('Pair available')
    else:
        print('No elements in list available')
    t2 = time.time()
    print(t2-t1, 'lin')


# linear_approach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
#                 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 35, 36], 33)


def linear_approach_unsorted(li, nbr):
    t1 = time.time()
    complement_set = set([])
    found = False
    for i in range(len(li)):
        complement = nbr - li[i]
        if complement in complement_set:
            found = True
        else:
            complement_set.add(li[i])
    if found:
        print('Pair available')
    else:
        print('No elements in list available')
    t2 = time.time()
    print(t2-t1, 'unsort')


# linear_approach_unsorted(
#     [5, 3, 5, 7, 65, 3, 55, 3, 22, 33, 11, 44, 53, 22, 1, 5], 33)

########################################################################################################################
# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For example:
# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'i']
# should return false
#
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']
# should return true

# O(n*m)


def brute_force_array(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return True
    return False


def better_finder_array(arr1, arr2):
    set1 = set(arr1)
    for index in range(len(arr2)):
        if arr2[index] in set1:
            return True
    return False


print(brute_force_array(array1, array2))

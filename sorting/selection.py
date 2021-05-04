def selection(li):
    for i in range(li):
        smallest = li[i]
        smallest_index = i
        for j in range(li):
            if li[j] < smallest:
                smallest = li[j]
                smallest_index = j
    temp = li[i]
    li[i] = smallest
    li[smallest_index] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selection(numbers)
print(numbers)

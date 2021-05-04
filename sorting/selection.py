def selection(li):
    for i in range(len(li)):
        temp = li[i]
        smallest_index = i
        for j in range(i+1, len(li)):
            if li[j] < li[smallest_index]:
                smallest_index = j
        li[i] = li[smallest_index]
        li[smallest_index] = temp
    return li


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selection(numbers))

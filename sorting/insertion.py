def insertion(li):
    length = len(li)
    last = li[0]
    for i in range(1, length):
        if li[i] < last:
            temp = li.pop(i)
            for j in range(0, i):
                if temp < li[j]:
                    li.insert(j, temp)
                    break
        last = li[i]
    return li


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(insertion(numbers))

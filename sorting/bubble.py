def bubble(arr):
    length = len(arr)
    for _ in range(0, length):
        for j in range(0, length-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
bubble(numbers)
print(numbers)

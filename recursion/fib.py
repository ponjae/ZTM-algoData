def recursive_fib(n):
    if n < 2:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


def iterative_fib(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n]


print(recursive_fib(8))
print(iterative_fib(8))

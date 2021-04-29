def recursive_factorial(num):
    if num == 0:
        return 1
    else:
        return num * recursive_factorial(num-1)


def iterative_factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result


print(recursive_factorial(6))

print(iterative_factorial(6))

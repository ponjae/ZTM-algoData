# Task: Create a function that reverses a string:
# 'Hi my name is Pontus' should be -->  'sutnoP si eman ym iH'

# This solution should be O(n)
def stringReverser(string):
    if not isinstance(string, str):
        return 'something is wrong here'
    if len(string) < 2:
        return string
    li = []
    for index in range(len(string) - 1, -1, -1):
        li.append(string[index])
    return ''.join(li)


print(stringReverser('Pontus was here'))

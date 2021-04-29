def recursive_reverser(string):
    if string == '':
        return ''
    else:
        return recursive_reverser(string[1:]) + string[0]


def iterative_reverser(string):
    word = ''
    for i in range(0, len(string)):
        word = string[i] + word
    return word


print(recursive_reverser('yoyo mastery'))
print(iterative_reverser('yoyo mastery'))

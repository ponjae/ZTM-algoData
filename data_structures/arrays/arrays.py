strings = ['a', 'b', 'c', 'd']
# 4 * 4 = 16 bytes of storage

strings[2]  # O(1)

# push
strings.append('e')  # O(1)

# pop
strings.pop()   # O(1)
strings.pop()

# add first element
# O(n) måste flytta om resten av arrayn i minnet, dvs gå igenom alla element i arrayn
strings.insert(0, 'x')

# add element at chosen index

# O(n) måste flytta om resten, i värsta fall hela arrayn
strings.insert(2, 'alien')

print(strings)

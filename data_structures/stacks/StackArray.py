class ArrayStack:
    def __init__(self):
        self.innerList = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.innerList[-1]

    def push(self, value):
        self.innerList.append(value)

    def pop(self):
        if len(self.innerList):
            self.innerList.pop()
        else:
            return 'Stack empty!'


stack = ArrayStack()

stack.push('Discord')
stack.push('Udemy')
stack.push('Google')
print(stack)
print(stack.peek())
stack.pop()
stack.pop()
stack.push('Microsoft')
print(stack)
stack.pop()
stack.pop()
print(stack.pop())

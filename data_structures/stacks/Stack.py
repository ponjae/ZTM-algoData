class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None
        elif self.length == 1:
            value = self.top.value
            self.top = None
            self.bottom = None
            self.length -= 1
            return value
        else:
            value = self.top.value
            self.top = self.top.next
            self.length -= 1
            return value

    def isEmpty(self):
        return self.length == 0

    def print_stack(self):
        curr = self.top
        while curr != None:
            print(f'{curr.value} -> ', end='')
            curr = curr.next


stack = Stack()
stack.push('Discord')
stack.push('Udemy')
stack.push('Google')
print(stack.peek(), ' peeking')
print(stack.pop(), 'popping')
print(stack.pop(), 'popping')

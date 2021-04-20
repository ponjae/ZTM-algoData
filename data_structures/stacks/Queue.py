class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_populated(self):
        return self.size > 0

    def peek(self):
        if self.is_populated():
            return self.first.value
        else:
            return 'Queue empty'

    def enqueue(self, value):
        n = Node(value)
        if not self.is_populated():
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n
        self.size += 1

    def dequeue(self):
        if not self.is_populated():
            return 'Queue already empty'
        elif self.size == 1:
            value = self.first.value
            self.first = None
            self.last = None
            self.size -= 1
            return value
        else:
            value = self.first.value
            self.first = self.first.next
            self.size -= 1
            return value

    def print_queue(self):
        curr = self.first
        while curr != None:
            print(curr.value)
            curr = curr.next


q = Queue()
q.enqueue('Testing')
q.enqueue('if')
q.enqueue('this')
q.enqueue('works')
q.print_queue()
q.dequeue()
print(q.dequeue())
print('*' * 50)
q.print_queue()

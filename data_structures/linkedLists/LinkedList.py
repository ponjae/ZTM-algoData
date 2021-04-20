# 10 --> 5 --> 16

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        n = Node(value)
        if self.head == None:
            self.head = n
            self.tail = n
            self.length += 1
        else:
            self.tail.next = n
            self.tail = n
            self.length += 1

    def prepend(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n
        self.length += 1

    def insert(self, value, index):
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            n = Node(value)
            current = self.head
            for _ in range(index-1):
                current = current.next
            n.next = current.next
            current.next = n
            self.length += 1

    def printList(self):
        arr = []
        current = self.head
        while current != None:
            arr.append(current.value)
            current = current.next
        print(arr)

    def remove(self, index):
        if index >= self.length:
            print('Index out of bounds')
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            current = self.head
            for i in range(self.length-1):
                if i == index - 1:
                    deleteNode = current.next
                    current.next = deleteNode.next
                    self.length -= 1
                    break
                current = current.next

    def reverse(self):
        if self.head.next == None:
            return self.head

        first = self.head
        self.tail = self.head
        second = first.next
        while second != None:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first


l = LinkedList()
l.append(10)
l.printList()
l.append(5)
l.printList()
l.append(6)
l.printList()
l.prepend(1)
l.printList()
l.insert(99, 2)
l.printList()
l.insert(34, 23)
l.printList()
l.insert(67474, 1)
l.printList()
l.reverse()
l.printList()
l.reverse()
l.printList()

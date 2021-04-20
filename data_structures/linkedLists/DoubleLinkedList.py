class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        n = Node(value)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.length += 1

    def prepend(self, value):
        n = Node(value)
        n.next = self.head
        self.head.prev = n
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
            current.next.prev = n
            current.next = n
            n.prev = current
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
            self.head.prev = None
            self.length -= 1
        else:
            current = self.head
            for i in range(self.length-1):
                if i == index - 1:
                    deleteNode = current.next
                    current.next = deleteNode.next
                    deleteNode.next.prev = current
                    self.length -= 1
                    break
                current = current.next


d = DoubleLinkedList()
d.append(10)
d.printList()
d.append(5)
d.printList()
d.append(6)
d.printList()
d.prepend(1)
d.printList()
d.insert(99, 2)
d.printList()
d.insert(34, 23)
d.printList()
d.insert(67474, 1)
d.printList()
d.remove(2)
d.printList()
d.remove(0)
d.printList()

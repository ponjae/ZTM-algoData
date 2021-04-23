class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            curr_node = self.root
            while True:
                if data < curr_node.value:
                    # Left
                    if curr_node.left == None:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left
                elif data > curr_node.value:
                    # Right
                    if curr_node.right == None:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right

    def lookup(self, value):
        curr = self.root
        while curr != None:
            if curr.value == value:
                return True
            elif curr.value > value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def remove(self, value):
        if self.root == None:
            return False
        currNode = self.root
        parent = None
        while currNode != None:
            if value < currNode.value:
                parent = currNode
                currNode = currNode.left
            elif value > currNode.value:
                parent = currNode
                currNode = currNode.right
            elif value == currNode.value:

                if currNode.right == None:
                    if parent == None:
                        self.root = currNode.left
                    else:
                        if currNode.value < parent.value:
                            parent.left = currNode.left
                        elif currNode.value > parent.value:
                            parent.right = currNode.left

                elif currNode.right.left == None:
                    currNode.right.left = currNode.left
                    if parent == None:
                        self.root = currNode.right
                    else:
                        if currNode.value < parent.value:
                            parent.left = currNode.right
                        elif currNode.value > parent.value:
                            parent.right = currNode.right
                else:
                    leftmost = currNode.right.left
                    leftMostParent = currNode.right
                    while leftmost.left != None:
                        leftMostParent = leftmost
                        leftmost = leftmost.left

                    leftMostParent.left = leftmost.right
                    leftmost.left = currNode.left
                    leftmost.right = currNode.right

                    if parent == None:
                        self.root = leftmost
                    else:
                        if currNode.value < parent.value:
                            parent.left = leftmost
                        elif currNode.value > parent.value:
                            parent.right = leftmost
            return True

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()

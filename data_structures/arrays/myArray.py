class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return item

    def delete(self, index):
        deletedItem = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        return deletedItem


myArray = Array()
print(myArray)
myArray.push(5)
myArray.push('hi')
myArray.push('hii')
myArray.push('hiii')
myArray.push('hiiii')
myArray.push('hiiiii')
myArray.push('hiiiiii')
print(myArray.delete(3))
print(myArray)

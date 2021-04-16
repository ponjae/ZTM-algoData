class My_hash_table:
    def __init__(self, bucket):
        """
                Create an array with a bucket size - which is derived from the load factor.
                The Load factor is a measure that decides when to increase the HashMap capacity to maintain the get() and put() operation complexity of O(1).
                The default load factor of HashMap is 0.75f (75% of the map size).
                Load Factor = (n/k)
                where n is the number of max number of elements that can be stored dict
                k is the bucket size
                Optimal Load factor is around (2/3) such that the effect of hash collisions is minimum 
                """
        self.bucket = bucket
        self.hashmap = [[] for i in range(self.bucket)]

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key):
        value = 0
        for i in range(len(key)):
            value = (value + ord(key[i])) % self.bucket
        return value

    def put(self, key, value):
        """
            value may already be present
        """
        hashed = self.hash(key)
        ref = self.hashmap[hashed]
        for index in range(len(ref)):
            if ref[index][0] == key:
                ref[index][1] = value
                return None
        ref.append([key, value])
        return None

    def get(self, key):
        """
            Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashed = self.hash(key)
        ref = self.hashmap[hashed]
        for elem in ref:
            if elem[0] == key:
                return elem[1]
        return -1

    def remove(self, key):
        """
            Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashed = self.hash(key)
        ref = self.hashmap[hashed]
        for index in range(len(ref)):
            if ref[index][0] == key:
                self.hashmap.pop([hashed][index])
                return None
        return None

    def keys(self):
        keys_array = []
        for i in range(len(self.hashmap)):
            if self.hashmap[i]:
                for item in self.hashmap[i]:
                    keys_array.append(item[0])
        return keys_array


h = My_hash_table(20)

h.put('grapes', 1000)
h.put('apples', 10)
h.put('ora', 300)
h.put('banan', 200)
print(h.keys())

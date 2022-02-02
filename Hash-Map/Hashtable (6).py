# O(1) for add, get, delete functions so it is emtremely fast
# Hash table by using list
'''
Hash Function

e.g.

index = len(key) - 1

|  0          |  1  |  2  |  3  |   4   |
| ['corn',2.38]| 
'''


class Hashmap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def gethash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        hash_key = self.gethash(key)
        key_value_pairs = [key, value]

        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value_pairs])
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[hash_key].append(key_value_pairs)
            return True

    def get(self, key):
        hash_key = self.gethash(key)
        cell_data = self.map[hash_key]
        if cell_data != None:
            for pair in cell_data:
                if pair[0] == key:
                    return pair[1]
        return False

    def delete(self, key):
        hash_key = self.gethash(key)
        if self.map[hash_key] is None:
            return False
        else:
            for i in range(len(self.map[hash_key])):
                if self.map[hash_key][i][0] == key:
                    self.map[hash_key].pop(i)
                    return True
        return False

    def existing_key(self):
        arr = []
        for i in range(len(self.map)):
            if self.map[i]:
                for j in range(len(self.map[i])):
                    arr.append(self.map[i][j][0])

        return arr

    def print(self):
        print("--phone data--")
        for item in self.map:
            print(str(item))


h = Hashmap()
h.add('Bob', '5670383')
h.add('Ming', 'jjjjj')
h.add('Bob', '567038')

h.print()
print(h.existing_key())

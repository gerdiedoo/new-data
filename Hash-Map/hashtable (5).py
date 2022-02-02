
class node:
    key = ""
    value = 0

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def set(self, value):
        self.value = value


    def output(self):
        print("'" + self.key + "' : '" + self.value + "'")



# Notes about hashTable
# As with all hashtables, hashTable loses efficiency rapidly once we approach full.
# hashTable utilizes linear probing
# This decision was made such that we avoid even more spatial inefficiency with a quadratic scheme
# Prior implementation of quadratic scheme resulted in unresolvable collisions at roughly 75% ~ 90% full table
# Also worth noting: hashTable is a fixed size and runs off of a list initialized to that size with None values
# This is not the most spatially efficient, but is rather convenient. Besides, if you're really dealing with
# a lot of values, you'd be better off with a hashmapped trie. This datastructure is designed for fixed convenience,
# pure and simple - it also reliably performs until 100% load factor.



class hashTable:
    # bucket is the container for all nodes
    bucket = []
    # we maintain a set of all keys to check for unique vals.
    # this way, we don't have to handle checking
    # at insert during hash function. Spatial tradeoff for speed & convenience.
    keys = set([])
    # cap size of hashTable. Fixed, set at instantiation
    size = 0
    __loadSum = 0
    # load value
    __loadFactor = 0.0

    # takes in size
    def __init__(self, size):
        self.keys = set([])
        self.size = size
        self.bucket = [None] * size
        self.__loadCalc();

    #we recalculate load on every operation
    #this function gets called at set operations and delete operations
    def __loadCalc(self):
        if (self.size == 0):
            self.__loadFactor = 0
        else:
            self.__loadFactor = self.__loadSum/self.size

    # returns value associated with key
    def get(self, k):
        k = str(k);
        if (k in self.keys):
            i = 0
            hashed = (hash(k) + i) % self.size
            while(self.bucket[hashed] != None):
                if(self.bucket[hashed].key != k):
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    return self.bucket[hashed].value
            return None
        else:
            return None

    # sets value at given key. returns boolean indicating success or failure
    # we use linear probing for collision resolution
    def set(self, k, v):
        k = str(k);
        if (k in self.keys):
            i = 0
            hashed = (hash(k) + i) % self.size
            while(self.bucket[hashed] != None):
                if(self.bucket[hashed].key != k):
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    self.bucket[hashed].value = v
                    return True
        elif (self.__loadFactor == 1.0):
            return False
        else:
            newNode = node(k, v)
            i = 0;
            hashed = (hash(k) + i) % self.size;
            while(self.bucket[hashed] != None):
                hashed = (hash(k) + i) % self.size
                i += 1
            self.bucket[hashed] = newNode
            self.keys.add(k)
            self.__loadSum += 1
            self.__loadCalc()
            return True


    # deletes value at given key. returns value.
    def delete(self, k):
        k = str(k);
        if (k in self.keys):
            i = 0
            hashed = (hash(k) + i) % self.size
            while(self.bucket[hashed] != None):
                if(self.bucket[hashed].key != k):
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    tmp = self.bucket[hashed].value
                    self.bucket[hashed] = None
                    self.keys.remove(k)
                    self.__loadSum -= 1
                    self.__loadCalc()
                    return tmp;
            return None
        else:
            return None

    #returns load
    def load(self):
        return self.__loadFactor

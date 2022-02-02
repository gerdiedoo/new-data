from hash_stats import HashStats


class RoboHash:
    """
    RoboHash is a HashTable implementation that provides constant time lookups and O(N) insertion time.
    It uses Open Addressing with linear probing for Hash collision resolution
    """

    """Initializes RoboHash

    array_size -- the size of the table to start with, will double when reaching storage_threshold
    storage_threshold -- the ratio of hashed items to buckets. Array will double when threshold is exceeded
    """
    def __init__(self, array_size=1117, storage_threshold=0.7):
        self.storage_threshold = storage_threshold
        self.array_size = array_size
        self.storage = [None for _ in range(array_size)]
        self.stats = HashStats()

    def get_stats(self):
        return self.stats

    """ inserts a value into the hashtable

    key -- the key to be used to retrieve the value
    value -- the value associated with the key
    """
    def insert(self, key, value):
        self.stats.increment_count()
        self.__resize_if_needed()
        idx = self.__hash(key)
        while True:
            item = self.storage[idx]
            if item is None:
                # Found a spot
                self.storage[idx] = (key, value)
                break
            elif item[0] == key:
                # item already exists with the key, so override
                self.storage[idx] = (key, value)
                break
            else:
                self.stats.increment_collisions()
                if idx == self.array_size - 1:
                    idx = 0
                else:
                    idx += 1

    """ retrieves an item from the hashtable with the specified key """
    def get(self, key):
        idx = self.__hash(key)
        self.stats.increment_requests()

        while True:
            item = self.storage[idx]
            self.stats.increment_seeks()
            if item is None:
                # item is not in Hash Table
                return None
            elif item[0] == key:
                return item[1]
            else:
                if idx == self.array_size - 1:
                    idx = 0
                else:
                    idx += 1

    def __hash(self, key):
        return hash(key) % self.array_size

    def get_hash(self, key):
        return self.__hash(key)

    def __resize_if_needed(self):
        if (self.stats.count / self.array_size) > self.storage_threshold:
            self.__resize()

    def __resize(self):
        # this could be improved if instead of just doubling we found the next closest prime number
        new_size = (self.array_size * 2) + 1
        new_hash = RoboHash(new_size)
        self.stats.increment_resizes()

        for item in self.storage:
            if item is not None:
                new_hash.insert(item[0], item[1])

        self.storage = new_hash.storage
        self.array_size = new_size

    def pretty_print(self):
        for i in range(0, self.array_size):
            item = self.storage[i]
            if item is not None:
                print("[" + str(i) + "] Key: " + str(item[0]) + " Value: " + str(item[1]))
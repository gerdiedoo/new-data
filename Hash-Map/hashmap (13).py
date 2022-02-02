from types import *

class hashmap(object):
    """ 
        Constructor
        
        Creates a fixed size hashmap that can contain up to size items
        The number of buckets is the smallest power of two that is bigger
        than size. This minimizes collisions while also optimizing for memory
        usage.

        Raises TypeError if size isn't an int
        Raises ValueError if size is less than 1
    """
    def __init__(self, size):
        if not(type(size) is IntType):
            raise TypeError('Size must be an int')
        if size < 1:
            raise ValueError('Invalid HashMap size')
        # number of buckets is smallest power of 2 >= size
        buckets = 1
        while buckets < size:
            buckets <<= 1
        # store size, number of buckets, current number of items
        self.size = size
        self.buckets = buckets
        self.items = 0
        # creates hashmap using separate chaining to deal with collisions
        self.hashmap = [[] for i in xrange(buckets)]

    """ 
        Set
    
        Inserts a key/value pair into the hashmap. Deals with collisions
        by using separate chaining. If a key is already in the hashmap,
        the value is overwritten and the number of items is not incremented.
        
        Returns False if hashmap is full
        Returns True if key/value pair is successfully added
    """
    def set(self, key, value):
        # hashmap is full
        if self.items == self.size:
            return False
        else:
            bucket = self.hashmap[key.__hash__() % self.buckets]
            # iterate over bucket in hashmap to see if key is already in hashmap
            for idx, (k, v) in enumerate(bucket):
                # overwrite value if key already in hashmap
                if k == key:
                    bucket[idx] = (key, value) 
                    return True
            # inserts key/value pair into bucket
            bucket.append((key, value))
            self.items += 1
            return True
    """
        Get

        Gets the value associated with the key that is stored in the hashmap

        Returns the value if the key is in the hashmap.
        Returns None if the key is not in the hashmap or the value is not set.
    """
    def get(self, key):
        # iterate over bucket in hashmap
        for k, v in self.hashmap[key.__hash__() % self.buckets]:
            if k == key:
                return v
        return None

    """
        Delete

        Deletes the value associated with a key in a hashmap

        Returns the value if the key was in the hashmap with a value.
        Returns None if the key was not in the hashmap or had no value
    """
    def delete(self, key):
        bucket = self.hashmap[key.__hash__() % self.buckets]
        # iterate over bucket in hashmap
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                # if key is found, remove value and return value
                bucket[idx] = (k, None)
                return v
        return None

    """
        Load

        Returns the load factor of the hashmap
    """
    def load(self):
        # items is always <= self.size and self.size is always <= self.buckets
        return float(self.items) / self.buckets

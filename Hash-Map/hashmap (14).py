# Implementation of the Map ADT using closed hashing and a probe with double hashing.
from arrays import Array

class HashMap:
    # Defines constants to represent the status of each table entry
    UNUSED = None
    EMPTY = _MapEntry( None, None)

    # Creates an empty map instance.
    def __init__( self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - (len(self._table) // 3)

    # Returns the number of entries in the map.
    def __len__(self):
        return self._count

    # Determines if the map contains the given key.
    def __contains__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None


    # Adds a new entry to the map if the key does not exist. Otherwise
    # ,the new value replaces the current value associated with the key.
    def add(self, key, value):
        if key in self:
            slot = self._findSlot(key, False)
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot(key, True)
            self._table[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True

    # Returns the value associated with the key.
    def valueOf(self, key):
        slot = self._findSlot(key, False)
        assert slot is not None, "Invalid map key"
        return self._table[slot].value

    # Removes the entry associated with the key.
    # return True when success this remove.
    def remove(self, key):
        slot = self._findSlot(key, False)
        if slot is not None:
            self._table[slot] = EMPTY
            self._count -= 1
            return True
        return False


    # Returns an iterator for traversing the keys in the map.
    def __iter__(self):
        return self
        
    # 
    def __next__(self):
        pass
        




    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added.
    def _findSlot(self, key, forInsert):
        # Compute the home slot and the step size.
        slot = self._hash1(key)
        step = self._hash2(key)

        # Probe for the key.
        M = len(self._table)
        while self._table[slot] is not UNUSED:
            if forInsert and \
                (self._table[slot] is EMPTY):
                return slot
            elif not forInsert and \
                (self._table[slot] is not EMPTY and self._table[slot].key == key):
                return slot
            else:
                slot = (slot + step) % M

        # because of rehash by self._maxCount
        # we can assert always there is an empty slot forInsert
        if forInsert and self._table[slot] is UNUSED:
            return slot

    # Rebuilds the hash table
    def _rehash(self):
        # Create a new larger table
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array(newSize)

        # Modify the size attributes
        self._count = 0
        self._maxCount = newSize - (newSize // 3)

        # Add the keys from the original array to the new table.
        for entry in origTable:
            if entry is not UNUSED and entry is not EMPTY:
                slot = self._findSlot(entry.key, True)
                self._count += 1
                self._table[slot] = entry






    # The main hash function for mapping keys to table entries.
    def _hash1(self, key):
        # we use hash(). so the key have to be hashable key.j
        return abs(hash(key)) % len(self._table)

    # The second hash function used with double hashing probes.
    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)


    def tableSize(self):
        return len(self._table)

    def getTable(self):
        return self._table

# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__( self, key, value):
        self.key = key
        self.value = value


# iterator class for HashMap
class _HashMapIter:
    def __init__(self, hashMap):
        self.hashMap = hashMap
        self.idx = 0
    def __next__(self):
        table = self.hashMap.getTable()
        while self.idx < len(table):
            if table[self.idx] is not UNUSED or table[self.idx] is not EMPTY:
                self.idx += 1
                return table[self.idx - 1].key
            self.idx += 1
            
        raise StopIteration

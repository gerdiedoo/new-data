from linked_list import LinkedList


class HashMap(object):


    # Initialize hash map with a default store of 8 buckets, each of which
    # is a linked list. While loop is used to create a new LinkedList object
    # each time
    def __init__(self, num_buckets=None):
        if num_buckets is None:
            num_buckets = 8

        self.store = []

        while len(self.store) < num_buckets:
            self.store.append(LinkedList())

        self.count = 0


    # Check if the linked list corresponding to that key, has that key
    def include(self, key):
        return self.bucket(key).include(key)


    # Method to implement bracketing into a hash map by key e.g. hash[key]
    def __getitem__(self, key):
        return self.bucket(key).get(key)


    # Method to implement setting values in a hash map through e.g. hash[k] = v
    def __setitem__(self, key, val):
        linked_list = self.bucket(key)

        if self.include(key):
            linked_list.update(key, val)
        else:
            if self.count == len(self.store):
                self.resize()
            linked_list.append(key, val)
            self.count = self.count + 1


    # Longform version of setting a key-value pair
    def set(self, key, val):
        self[key] = val


    # Longform version of getting a value for a key
    # Default parameter allows for a default value to be returned
    # if key is not in the hash map
    def get(self, key, default=None):
        if self[key]:
            return self[key]
        else:
            return default


    # Delete key-value pair: look for a link in the correct linked list
    # that has that key, that remove it
    def delete(self, key):
        linked_list = self.bucket(key)

        if linked_list.include(key):
            linked_list.remove(key)
            self.count -= 1


    # Implement resizing the hash map's store so that inserting key-value
    # pairs is O(1) amortized
    def resize(self):
        old_store = self.store
        self.count = 0
        self.store = []

        while len(self.store) < len(old_store) * 2:
            self.store.append(LinkedList())

        for linked_list in old_store:
            link = linked_list.first()
            while link != linked_list.tail:
                self[link.key] = link.val
                link = link.next


    # Helper method for finding the correct linked list for a given key
    def bucket(self, key):
        return self.store[hash(key) % len(self.store)]


    # Method to implement string representation of hash - e.g. str(hash)
    # Useful for debugging
    def __str__(self):
        pairs = []

        i = 0

        while i < len(self.store):
            linked_list = self.store[i]
            if not linked_list.empty():
                pairs.append(str(linked_list))

            i = i + 1

        return ", ".join(pairs)

    def keys(self):
        key_items = []

        i = 0

        while i < len(self.store):
            linked_list = self.store[i]
            links = linked_list.keys()
            key_items = key_items + links
            i += 1

        return key_items

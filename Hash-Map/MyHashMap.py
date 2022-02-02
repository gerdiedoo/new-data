from Entry import Entry
from LinkedList import SingleEntryLinkedList

DEFAULT_MAXIMUM_LOAD_FACTOR = 0.75
DEFAULT_MAXIMUM_UNLOAD_FACTOR = 0.1
MAXIMUM_CAPACITY = 1 << 30


class MyHashMap(object):

    """
    My hash map implementation 
    Author: Nikta Khomenko
    """

    DEFAULT_INITIAL_CAPACITY = 4

    def __init__(self, capacity=DEFAULT_INITIAL_CAPACITY, load_factor=DEFAULT_MAXIMUM_LOAD_FACTOR):

        if capacity > MAXIMUM_CAPACITY:
            self.capacity = MAXIMUM_CAPACITY

        else:
            self.capacity = self.trim_power_of2(capacity)

        self.thresholdLoadFactor = load_factor
        self.thresholdUnloadFactor = DEFAULT_MAXIMUM_UNLOAD_FACTOR
        self.size = 0
        self.table = [SingleEntryLinkedList() for i in range(capacity)]

    def trim_power_of2(self, initial_capacity):  # trims the capacity to power of 2
        capacity = 1
        while capacity < initial_capacity:
            capacity <<= 1
        return capacity

    def hash_code(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.capacity

    def clear(self):
        self.size = 0
        self.remove_entries()

    def remove_entries(self):
        for entry_list in self.table:
            if entry_list.list_length != 0:
                entry_list.head = None

    def contains_key(self, key):
        index = self.hash_code(key)
        if self.table[index].list_length != 0:
            return self.table[index].unordered_search_key(key)

    def contains_value(self, value):
        for entry_list in self.table:
            if entry_list.list_length != 0:
                if entry_list.unordered_search_value(value):
                    return True
        return False

    def get(self, key):  # returning an element by specified key
        if key is not None:
            index = int(self.hash_code(key))
            if self.table is not None:
                if self.table[index].list_length != 0:
                    return self.table[index].unordered_search_get_entry_by_key(key)
        return None

    def put(self, key, value):  # adding an element to the map by specified key
        index = int(self.hash_code(key))
        if (self.get(key) is not None) & (self.table[index].list_length != 0):  # if the key already exists
            if self.table[index].unordered_search_key(key):
                return self.table[index].override_list_item(Entry(key, value))

        #  if index is taken we make a linked list
        self.table[index].add_list_item(Entry(key, value))
        self.size = + 1

        # check if need to resize
        if self.size + 1 >= self.capacity * self.thresholdLoadFactor:  # if need rehash
            if self.capacity == MAXIMUM_CAPACITY:
                RuntimeError("Exceeding maximum capacity")
            self.resize()

        return None

    def entry_set(self):  # return set of the entries in the map
        e_set = set()
        for entry_list in self.table:
            current_node = entry_list.head
            while current_node is not None:
                e_set.add(current_node.data)
                # jump to the linked node
                current_node = current_node.next
        return e_set

    def resize(self):
        do_resize = False
        if self.size / self.capacity > self.thresholdLoadFactor:
            self.capacity = self.capacity * 2
            self.thresholdLoadFactor = self.capacity * 0.75
            do_resize = True

        if self.size / self.capacity < self.thresholdUnloadFactor:
            self.capacity = self.capacity / 2
            self.thresholdLoadFactor = self.capacity * 0.75
            do_resize = True

        if do_resize:
            entry_set_old_table = self.entry_set()
            self.table = [SingleEntryLinkedList() for i in range(int(self.capacity))]

            for entry in entry_set_old_table:
                self.put(entry.key, entry.val)

    def is_empty(self):  # returning if the map contains values or not
        return self.size == 0

    def key_set(self):  # returning a set of the keys in this map
        k_set = set()
        for entry in self.entry_set():
            k_set.add(entry.key)
        return k_set

    def map_copy(self, map_to_copy):  # coping a full map to this map
        m_set = map_to_copy.entry_set()
        for entry in m_set:
            self.put(entry.key, entry.val)

    def remove(self, key):  # removing element by specified key
        index = self.hash_code(key)
        last_entry = self.table[index].head
        while last_entry.data.key != key:
            last_entry = last_entry.next
        old_value = last_entry.data.val
        last_entry.data = None
        self.size -= 1

        if self.size + 1 <= self.capacity * self.thresholdUnloadFactor:
            self.resize()

        return old_value

    def value_set(self):  # return a set consisting of the values in the map
        v_list = set()
        for entry in self.entry_set():
            v_list.add(entry.val)
        return v_list

    def print_map(self):
        for entry_list in self.table:
            entry_list.output_list()

    def generator(self):
        for index in range(-1, len(self.table) - 1, 1):
            yield self.table[index]



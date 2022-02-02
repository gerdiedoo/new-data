"""
Provides a simple bidirectional hashmap backed by dictionaries.
"""


class BiMap:
    """
    A simple bidirectional hashmap implementation.
    """

    def __init__(self, dictionary=None):
        """Create a new BiMap."""
        self.key_to_value = dict()
        self.value_to_key = dict()

        if dictionary:
            for key in dictionary:
                self.add_key(key, dictionary[key])

    def __iter__(self):
        """Iterate over keys."""
        return self.key_to_value.__iter__()

    def __len__(self):
        return len(self.key_to_value)

    def add_key(self, key, value):
        """Add a new (key, value) pair."""
        self.key_to_value[key] = value
        self.value_to_key[value] = key

    def add_value(self, value, key):
        """Add a new (value, key) pair."""
        self.add_key(key, value)

    def update_by_key(self, dictionary):
        """Add multiple (key, value) pairs. Overwrites collisions."""
        for key, value in dictionary.items():
            self.add_key(key, value)

    def update_by_value(self, dictionary):
        """Add multiple (value, key) pairs. Overwrites collisions."""
        for value, key in dictionary.items():
            self.add_key(key, value)

    def get_key(self, key):
        """Get the value from a key."""
        return self.key_to_value[key]

    def get_value(self, value):
        """Get the key from a value."""
        return self.value_to_key[value]

    def remove_key(self, key):
        """Remove a pair by it's key."""
        del self.value_to_key[self.key_to_value[key]]
        del self.key_to_value[key]

    def remove_value(self, value):
        """Remove a pair by it's value."""
        self.remove_key(self.get_value(value))

    def clear(self):
        """Remove all pairs."""
        self.key_to_value.clear()
        self.value_to_key.clear()

    def pop_key(self, key):
        """Remove a pair by it's key and return the value."""
        value = self.get_key(key)
        self.remove_key(key)
        return value

    def pop_value(self, value):
        """Remove a pair by it's value and return the key."""
        key = self.get_value(value)
        self.remove_value(value)
        return key

    def get_key_to_value(self):
        """Get the key_to_value dictionary."""
        return self.key_to_value

    def get_value_to_key(self):
        """Get the value_to_key dictionary."""
        return self.value_to_key

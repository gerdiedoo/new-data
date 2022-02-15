# -*- coding: utf-8-*-


class Node(object):
    """A Node containing a value and avalible pointers to other nodes."""
    def __init__(self, val, next_node=None, prev_node=None):
        """Node initation method."""
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node


class DLL(object):
    """Double Linked List class that inherits LinkedList."""

    def __init__(self, iter=None):
        """Constructor for Double Linked List."""
        self.tail = None
        self.head = None
        if iter:
            for val in iter:
                self.insert(val)

    def insert(self, val):
        """Insert a value at the head of the list."""
        new_node = Node(val=val, next_node=self.head)
        if self.head:
            self.head.prev_node = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def append(self, val):
        """Append a value at the tail of the list."""
        new_node = Node(val=val, prev_node=self.tail)
        if self.tail:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def pop(self):
        """Pop the value at the head of the list."""
        try:
            rtn_value = self.head.val
            new_head = self.head.next_node
            self.head = new_head
            if self.head is None:
                self.tail = None
                return rtn_value
            self.head.prev_node = None
            return rtn_value
        except AttributeError:
            return None

    def shift(self):
        """Remove the value at the tail of the list."""
        try:
            rtn_value = self.tail.val
            new_tail = self.tail.prev_node
            self.tail = new_tail
            if self.tail is None:
                self.head = None
                return rtn_value
            self.tail.next_node = None
            return rtn_value
        except AttributeError:
            return None

    def remove(self, val):
        """Remove first instance of val from the list starting from head."""
        val_search = self.search(val)
        if val_search is None:
            raise ValueError
        try:  # Runs if removing node from middle.
            val_search.prev_node.next_node = val_search.next_node
            val_search.next_node.prev_node = val_search.prev_node
        except AttributeError:
            try:  # Runs if removing head or tail.
                if self.head == val_search:
                    self.head = val_search.next_node
                    self.head.prev_node = None
                if self.tail == val_search:
                    self.tail = val_search.prev_node
                    self.tail.next_node = None
            except AttributeError:
                # Runs if removing last node.
                self.head = None
                self.tail = None
        return val_search.val

    def search(self, val):
        """Search and return the Node with value val if in the list."""
        step_head = self.head
        while step_head:
            if step_head.val == val:
                return step_head
            step_head = step_head.next_node
        else:
            return None

    def to_string(self):
        """Return a string representation of the list."""
        rtn_string = u"("
        step_head = self.head
        while step_head:
            if step_head.next_node is None:
                rtn_string += str(step_head.val)
                break
            rtn_string += str(step_head.val) + u", "
            step_head = step_head.next_node
        rtn_string += u")"
        return rtn_string

    def size(self):
        """Return the length of the list."""
        count = 0
        step_head = self.head
        while step_head:
            count += 1
            step_head = step_head.next_node
        return count

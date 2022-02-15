"""Implements a doubly-linked list."""
import linked_list


class Node(linked_list.Node):
    """A single node from a doubly-linked list."""

    def __init__(self, val, nxt=None, prev=None):
        """Construct a new Node."""
        super(Node, self).__init__(val, nxt)
        self.prev = prev


class DLL(linked_list.LinkedList):
    """List of values stored in nodes linked in two directions."""

    def __init__(self, iterable=None):
        """Construct a Doubly-Linked List (DLL)."""
        self.tail = None
        super(DLL, self).__init__(iterable)

    def push(self, val):
        """Insert the value val at the head of the list."""
        old_head = self.head
        self.head = Node(val, nxt=self.head)
        self.length += 1
        if old_head:
            old_head.prev = self.head
        else:
            self.tail = self.head

    def append(self, val):
        """Append the value val at the tail of the list."""
        old_tail = self.tail
        self.tail = Node(val, prev=self.tail)
        self.length += 1
        if old_tail:
            old_tail.nxt = self.tail
        else:
            self.head = self.tail

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        val = super(DLL, self).pop()
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def shift(self):
        """Remove the last value from the tail of the list and return it."""
        if not self.tail:
            raise IndexError('Cannot shift from empty list.')
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.nxt = None
        else:
            self.head = None
        self.length -= 1
        return val

    def remove(self, val):
        """Remove the first instance of val found in the list, starts at head.

        Raises a ValueError if value is not in the list.
        """
        if not self.head:
            raise ValueError('Cannot remove from empty list.')
        if self.head.val == val:
            self.pop()
            return
        curr = self.head
        while curr.nxt:
            if curr.val == val:
                curr.prev.nxt, curr.nxt.prev = curr.nxt, curr.prev
                self.length -= 1
                return
            curr = curr.nxt
        if self.tail.val == val:
            self.shift()
            return
        raise ValueError('Value is not in list.')

"""Implements a linked list."""


class Node(object):
    """A single node from a linked list."""

    def __init__(self, val, nxt=None):
        """Construct a new Node."""
        self.val = val
        self.nxt = nxt


class LinkedList(object):
    """List of values stored in nodes linked to each other in one direction."""

    def __init__(self, iterable=None):
        """Contruct a new LinkedList."""
        self.head = None
        self.length = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def __len__(self):
        """Overwrite the default return for len function."""
        return self.length

    def __str__(self):
        """Overwrite the default return for print function."""
        return self.display()

    def size(self):
        """Get the size of the LinkedList."""
        return len(self)

    def push(self, val):
        """Add another value to the front of the list."""
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        """Remove the first node and return it's value."""
        if not self.head:
            raise IndexError('Cannot pop from empty list.')
        val = self.head.val
        self.head = self.head.nxt
        self.length -= 1
        return val

    def search(self, val):
        """Find the node that has the given value."""
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.nxt

    def remove(self, node):
        """Remove the given node from the LinkedList."""
        if self.head is node:
            self.head = self.head.nxt
            self.length -= 1
            return

        curr = self.head
        while curr:
            if curr.nxt is node:
                curr.nxt = node.nxt
                self.length -= 1
                return
            curr = curr.nxt

        raise ValueError('Node is not in list.')

    def display(self):
        """Display LinkedList as if it were a tuple literal."""
        curr = self.head
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.nxt
        return tuple(output).__str__()

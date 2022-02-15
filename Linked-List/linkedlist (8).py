import element

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
    def get_position(self, position):
        if not self.head:
            return None
        elif position == 1:
            return self.head
        else:
            current = self.head
            while (position > 1):
                current = current.next
                if current == None:
                    return None
                position = position - 1
            return current

    """Insert a new node at the given position.
            Assume the first position is "1".
            Inserting at position 3 means between
            the 2nd and 3rd elements."""
    def insert(self, new_element, position):
        if not self.head:
            self.head = new_element
            return

        try:
            prev_element = self.get_position(position - 1)
            next_element = prev_element.next
            prev_element.next = new_element
            new_element.next = next_element
        except:
            raise Exception('Unable to insert element at this position.')

    """Delete the first node with a given value."""
    def delete(self, value):
        if value == self.head.value:
            new_head = self.head.next
            self.head = new_head
            return

        previous = self.head
        current = self.head.next

        while (previous.next != None):
            if (current.value == value):
                previous.next = current.next
                return
            current = current.next
            previous = previous.next
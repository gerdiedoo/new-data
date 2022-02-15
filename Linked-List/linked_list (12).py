from link import Link


class LinkedList(object):


    # Initialize a new LinkedList object. Use of sentinel nodes for head
    # and tail to prevent having to check for null when unshifting or
    # pushing links
    def __init__(self):
        self.head = Link()
        self.tail = Link()
        self.head.next = self.tail
        self.tail.prev = self.head


    # Method to allow for bracketing into linked list at a certain
    # position e.g. linked_list[3]
    def __getitem__(self, desired_index):
        current_index = 0
        link = self.first()
        while link != self.tail:
            if current_index == desired_index:
               return link
            link = link.next
            current_index += 1

        return None


    # First link in the linked list
    def first(self):
        return self.head.next


    # Last link in the linked list
    def last(self):
        return self.tail.prev


    # Returns boolean corresponding to whether the linked list is empty
    def empty(self):
        return self.first() == self.tail


    # Returns value for a link given a key
    def get(self, key):
        link = self.first()

        while link != self.tail:
            if link.key == key:
                return link.val
            link = link.next

        return None


    # Checks whether a link with given key is included in the linked
    # list
    def include(self, key):
        return not not self.find(key)


    # Append link to the end of the linked list. O(1)
    def append(self, key, val):
        old_prev = self.tail.prev

        new_link = Link(key, val)

        new_link.next = self.tail
        self.tail.prev = new_link

        new_link.prev = old_prev
        old_prev.next = new_link


    # Returns link if link found with that key
    def find(self, key):
        link = self.first()

        while link != self.tail:
            if link.key == key:
                return link
            link = link.next

        return None


    # Updates a link with a given key with the given value
    def update(self, key, val):
        link = self.find(key)
        if link:
            link.val = val

        return link


    # Removes a link with given key from the linked list
    def remove(self, key):
        link = self.find(key)
        if link:
            link.remove()

        return link


    # String representation of linked list - e.g. str(linked_list)
    def __str__(self):
        links = []
        link = self.first()

        while link != self.tail:
            links.append(str(link))
            link = link.next

        return ", ".join(links)

    def keys(self):
        links = []
        link = self.first()

        while link != self.tail:
            links.append(link.key)
            link = link.next

        return links

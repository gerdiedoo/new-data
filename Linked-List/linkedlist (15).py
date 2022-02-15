import collections

class Node():
    """
     Node representation in a singly linked list
    """
    def __init__(self, value):
        """
         Constructor
         Initialize with value and None next pointer

         value (any) -- any type of value containing actual data
        """
        self.value = value
        self.next = None

    def __repr__(self):
        return '%s(%r)' % ('Node', self.value)

class LinkedList(collections.MutableSequence):
    """
     Singly linked list class
     Provide index based operations as built-in list

     Example:
     linkedlist[0]        : get the first el
     linkedlist[5] = value: set the 6th el with new value
     del linkedlist[3]    : delete the 4th el
    """
    def __init__(self, iterable=None):
        """
        Initialize 3 attributes
        _len  -- Interger for the number of element in LinkedList
        _head -- Pointer to the first element
        _tail -- Pointer to the last element

        @param iterable -- Any iterable object(list, set etc.) to initialize the LinkedList
        """
        self._len = 0
        self._head = None
        self._tail = None
        if iterable is not None: # will automatically call append
            self += iterable

    def __repr__(self):
        """
        String representation for this linked list

        Example:
        Node(1)->Node(2)...
        """
        node = self._head
        _list = []
        while node:
            _list.append( str(node) )
            node = node.next
        #_list = [ str(self._getnode(i)) for i in range(len(self)) ]
        return '->'.join(_list)

    def _getnode(self, index):
        """
        Iterate the linked list to get a Node for the given index

        @param index -- Integer for index
        """
        if self._head is None: # empty
            return None
        if index >= self._len: # index out of range
            return None
        node = self._head
        i = 0
        while i < index:
            node = node.next
            #if node is None:
                #return None
            i += 1
        return node

    """
      Protocol for MutableSequence
      Provide index based operations
    """
    def __len__(self):
        return self._len
    def __getitem__(self, index):
        return self._getnode(index)
    def __setitem__(self, index, value):
        node = self._getnode(index)
        node.value = value
    def __delitem__(self, index):
        if index  == 0: # splice out the first, the second becomes the new head now
            self._head = self[0].next
        else:
            pre = self._getnode(index-1)
            node = self._getnode(index)
            # splice out the node by removing the pointer to it
            pre.next = node.next
            if node == self._tail:
                self._tail = pre

        self._len -= 1

    def append(self, value):
        """
        Append a new Node to the end of the linked list

        @param value -- value for creating a new Node
        """
        newnode = Node(value)
        if self._head is None:
            self._head = newnode
        else:
            # link the new node to the list
            self._tail.next = newnode
        # make tail point to new node
        self._tail = newnode
        self._len += 1

    def insert(self, index, value):
        """
        Insert a new Node at a given index

        @param index -- Integer for a position
        @param value -- value for the new Node object
        """
        newnode = Node(value)
        if index == 0: # at the beginning
            newnode.next = self._head
            self._head = newnode
            return
        elif index == len(self): # at the end, same as append
            self._tail.next = newnode
            self._tail = newnode
        else:
            # get the previous node of the inserted position
            node = self._getnode(index-1)
            # if index is invalid (not in list range)
            if node is None:
                return
            temp = node.next
            node.next = newnode
            newnode.next = temp

        self._len += 1

    def reverse_(self):
        def recurse(self, prev, node):
            if node is None:
                return
            # recursively go to the tail first
            recurse(self, node, node.next)
            if node == self._tail:
                self._head = node
            node.next = prev
            if prev is None:
                self._tail = node

        recurse(self, None, self._head)

    def reverse(self):
        prev, cur = None, self._head
        self._tail = cur
        while cur:
            # Change the next pointer to refer to its previous node
            temp = cur.next
            cur.next = prev
            # Move prev and cur pointer forward to change next node
            prev = cur
            cur = temp
        self._head = prev

if __name__ == '__main__':
    #iterable = [i for i in range(10)]
    #ll = LinkedList(iterable)
    #print ll
    #ll.reverse_()
    #print ll

    import timeit
    sp = 'from linkedlist import *; ll = LinkedList(range(1000000))'
    print timeit.repeat("ll.insert(0, 9)", setup=sp, number=5)

    print timeit.repeat("l.insert(0, 9)", setup='l = range(1000000)', number=5)

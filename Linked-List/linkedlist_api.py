#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0

    def debug_print(self):
        '''Prints a representation of the entire list.'''
        print('{} >>> {}'.format(
            self.size, ', '.join([str(item) for item in self])))

    def __iter__(self):
        '''Iterates through the linked list, implemented as a generator.'''
        for node in self._iter_nodes():
            yield node.value

    def _iter_nodes(self):
        '''Iterates through the nodes of the list, implemented as a generator.'''
        current = self.head
        while current != None:
            yield current
            current = current.next

    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        node = self.head
        if index > self.size - 1:
            raise ValueError(
                "{} is not within the bounds of the linked list".format(index))
        for i in range(index):
            node = node.next
        return node

    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        node = Node(item)
        node.next = None
        if self.head == None:
            self.head = node
            self.size += 1
            return
        for current in self._iter_nodes():
            if current.next == None:
                current.next = node
                self.size += 1
                return

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        new_node = Node(item)

        prev_node = self._get_node(index - 1)
        next_node = self._get_node(index)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = next_node
            prev_node.next = new_node
        self.size += 1

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        target_node = self._get_node(index)
        if target_node is not None:
            target_node.value = item

    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        target_node = self._get_node(index)
        if target_node is not None:
            return target_node.value

    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        target_node = self._get_node(index)
        if index == 0:
            self.head = target_node.next
            target_node.value = None
        else:
            prev_node = self._get_node(index - 1)
            prev_node.next = target_node.next
        self.size -= 1

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        node1 = self._get_node(index1)
        node2 = self._get_node(index2)
        node1.value, node2.value = node2.value, node1.value


######################################################
# A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)

## Linked List Class
## Author: Grant Gasser
## 7/17/2019

import node

class List():
    def __init__(self, head=None):
        """
        A linked list object need only consist of pointer to head node.
        """
        self._head = head

    def get_head(self):
        return self._head

    def append(self, data):
        """
        Push node with new data to the back of the linked list

        Args:
            data (int): data for a node to be added at end of list

        Returns:
            self: reference to itself for chaining
        """

        # given the data, so create the new node here in function
        new_node = node.Node(data)

        # if no nodes in list, new node is the head
        if not self._head:
            self._head = new_node

        else:
            temp = self._head

            # move along list to the end, then append
            while(temp.next):
                temp = temp.next

            temp.next = new_node # append

        return self


    def get_position(self, position):
        """
        Return node given particular position.

        Args:
            position (int): the position of the node where the head is 1

        Returns:
            a node (Node): the node at the position
        """
        if position < 1: # bad index
            return None

        # start at beginning of list
        current_pos = 1
        current = self._head


        if self._head:
            # iterate to position
            while current and current_pos < position:
                current = current.next
                current_pos += 1

            return current
        # if no list
        else:
            return None


    def insert(self, new_data, position):
        """
        Insert new node given new data at certain position.

        Args:
            new_data (int): the actual value of the new node.
            position (int): the position to insert. Ex. insert at position 4
                means inserting between current 3rd and 4th elements

        Returns:

        """
        new_node = node.Node(new_data)

        # assertions - need to brush up on assertions and throwing exceptions
        assert(position >= 1)
        assert(self._head)

        # start at head node
        current_pos = 1
        current = self._head

        # iterate to insertion position
        while current and current_pos < position - 1:
            current = current.next
            current_pos += 1

        # be careful, don't lose reference to next node
        if current:
            new_node.next = current.next
            current.next = new_node
        else:
            print('\nERROR: Could not insert node. Position', position, 'is out of bounds.')

    def delete(self, data):
        """
        Delete first node seen with given data.

        Args:
            data (int): data whose node should be deleted

        Returns:

        """
        current = self._head
        previous = None

        # iterate thru list until find a node with given data
        while current.data != data and current.next:
            previous = current
            current = current.next

            # found node with given data, delete
            if current.data == data:
                if previous:
                    previous.next = current.next # draw arrow past current, deleting it
                    current.next = None

                # previous never changed from None since only one node in list
                else:
                    self._head = current.next


    def reverse_list_iterative(self):
        """
        Reverse the direction of the arrows in the list. Iterative solution with
        three pointers: prev, curr, next. Time Complexity: O(N)
        """
        prev = None
        curr = self._head
        next = None

        # reverse the list until curr is None
        while curr:
            # swap
            next = curr.next
            curr.next = prev

            # move forward
            prev = curr
            curr = next


        #set head to last (now first) node
        self._head = prev


    def reverse_list_recursive(self, curr, prev=None, next=None):
        """
        Reverse the direction of the arrows in the list. Recursive solution with
        three pointers: prev, curr, next. Time Complexity: O(N)
        """
        if not curr: # base case, at the end of the list
            self._head = prev
        else:
            next = curr.next
            curr.next = prev

            # recursive call
            self.reverse_list_recursive(next, curr)


    def print_list(self):
        """
        Iterate through a print data of each node from list (start at head)
        """

        temp = self._head

        while(temp):
            print(temp)
            temp = temp.next

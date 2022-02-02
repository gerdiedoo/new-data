from node import Node


class LinkList:

    def __init__(self):
        self.first_node = None
        self.last_node = None

    def add_node(self, key, value):
        new_node = Node(key, value)
        new_node.key = key
        new_node.value = value
        self.append_new_node_to_list(new_node)

    def append_new_node_to_list(self, new_node):
        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
        elif self.last_node == self.first_node:
            self.last_node = new_node
            self.first_node.next = new_node
        else:

            self.last_node.next = new_node
            self.last_node = new_node

    def contains_value(self, value):
        current_node = self.first_node
        result = False
        while current_node is not None:
            if current_node.value == value:
                result = True
                break
            current_node = current_node.next
        return result

    def contains_key(self, key):
        current_node = self.first_node
        result = False
        while current_node is not None:
            if current_node.key == key:
                result = True
                break
            else:
                current_node = current_node.next
        return result

    def delete_node_with_key(self, key):
        previous_node = self.last_node
        current_node = self.first_node
        if (current_node.key == key) & (previous_node.key == key):
            self.last_node = None
            self.first_node = None
            return
        else:
            while current_node.next is not None:
                if current_node.key == key:
                    self._remove_node_from_list(current_node, previous_node)
                else:
                    current_node = current_node.next

    @staticmethod
    def _remove_node_from_list(current_node, previous_node):
        previous_node.next = current_node.next

    def clear(self):
        self.__init__()

# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:

    # Creating an empty list with an empty head
    def __init__(self):
        self.head = None

    # Push Function to add a node to the LinkedList
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


if __name__ == '__main__':

    linkedlist = LinkedList()

    # Loop to let user add nodes to the list
    newData = 0

    while newData != "fin":
        newData = input("Enter the number you want to add to the list, enter \"fin\" when you've finished:")
        if newData != "fin":
            linkedlist.push(newData)
            print(newData + " is added")

    # Loop that prints out each node
    currentNode = linkedlist.head

    print("All nodes off the Linked List:")
    while currentNode is not None:
        data = currentNode.data
        print(data)
        currentNode = currentNode.next

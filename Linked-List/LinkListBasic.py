class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def append(self, newElement):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newElement
        else:
            self.head = newElement
    #get position time complexity O(n)
    #get the node at a specific position
    def get_position(self, position):
        current = self.head
        current_pos = 1
        while current_pos <= position:
            if current_pos == position:
                return current
            current = current.next
            current_pos += 1
        return None
    #Insert element
    # Time complexity O(n)
    def insert_element(self, element, position):
        if position > 1:
            target_position = self.get_position(position - 1)
            element.next = target_position.next
            target_position.next = element
        else:
            element.next = self.head
            self.head = element
    def delete_element(self, element):
        current = self.head
        previous = None
        while current:
            if current.value == element:
                if not previous:
                    self.head = current.next 
                    return True
                
                else:
                    previous.next = current.next
            previous = current
            current = current.next
        return False

            
node1 = Node("Iron Man")
node2 = Node("Capitain America")
node3 = Node("Doctor Strange")
node4 = Node("Spider man")
node5 = Node("Rieder")
print("Node1 Value is {}".format(node1.value))
print("Node1 next Value is {}".format(node1.next))
print("Node2 Value is {}".format(node2.value))
print("Node2 next Value is {}".format(node2.next))
Avengers = LinkedList()
Avengers.append(node1)
print("Firt element in link list is {}".format(Avengers.head.value))
Avengers.append(node2)
print("After Iron Man is {}".format(Avengers.head.next.value))
print(Avengers.get_position(2).value)
Avengers.append(node3)
Avengers.append(node4)
Avengers.insert_element(node5, 4)
print(Avengers.get_position(4).value)
print(Avengers.get_position(5).value)
Avengers.delete_element("Rieder")
print(Avengers.get_position(4).value)
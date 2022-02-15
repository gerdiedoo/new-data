# NODE CLASS STARTS HERE
class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.prev = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def setData(self, data):
		self.data = data

	def setNext(self, next):
		self.next = next

	def setPrev(self, prev):
		self.prev = prev

# NODE CLASS ENDS HERE

# LINKED LIST CLASS STARTS HERE
# ADD: 1. AT THE BEGINING, 2. AT THE END, 3. AT nth POSITION
# DELETE: 1. AT THE BEGINING, 2. AT THE END, 3. AT nth POSITION
# REVERSE: 1. REVERSE USING ITERATIVE METHOD, 2. REVERSE USING RECURSION
# PRINT: 1. SIMPLE PRINT, 2. PRINT USING RECURSION, 3. REVERSE PRINT USING RECURSION 
class DoublyLinkedList:
	def __init__(self):
		self.head = None

	# Print the linked list
	def print(self):
		if self.head is None:
			print("linked list is empty, nothing to print")
			return

		current = self.head
		while current:
			print(current.data)
			current = current.next


	# Reverse print the linked list
	def reverse_print(self):
		if self.head is None:
			print("linked list is empty, nothing to print")
			return

		current = self.head
		while current.next != None:
			current = current.next

		while current !=None:
			print(current.data)
			current = current.prev


	# Add element at the begining
	def add_at_the_begining(self, data):
		node = Node(data)
		if self.head is None: #linked list is empty
			self.head = node
			return
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node
			# No need to do node.prev = None since newly intialized node already contains null in its next and prev parts

	# Add element at the end
	def add_at_the_end(self, data):
		node = Node(data)
		if self.head is None: #linked list is empty
			self.head = node
			return
		else:
			current = self.head
			while current.next != None:
				current = current.next

			current.next = node
			node.prev = current
			# No need to do node.next = None since newly intialized node already contains null in its next and prev parts
		
	# Inserts the element at the nth position
	# pos=0 will be considered invalid position
	# In a linked list of 4 elements, 2, 4, 6, 8 - pos=1 to pos=5 are valid positions,
	# where pos=1 inserts the element at the beginging of the list and pos=5 inserts the element at the end of the list
	def add_at_nth_position(self, data, pos):
		node = Node(data)
		
		if pos <= 0:
			print("Invalid position, it can not be less than or equal to 0")
			return
		elif pos == 1: # Insertion at the begining
				self.add_at_the_begining(data)
		else:
			current = self.head
			i=1
			while i < pos-1 and current != None: # If pos is 5 loop only 3 times so current node is one node behind the pos and do insert node after the current node
				current = current.next
				i = i+1

			if current is None: # If current became null that means pos is +2 higher than no. of elements in the linked list which is an invalid position
				print("Invalid position!!!")
				return
			elif current.next is None:
				self.add_at_the_end(data)
			else:
				node.next = current.next
				node.prev = current
				current.next.prev = node
				current.next = node
			

	#removes the element at the begining of the list
	def remove_at_the_begining(self):
		if self.head is None:
			print("List is empty, nothing to remove.")
		elif self.head.next is None: # There is only one element in the linked list
			temp = self.head
			self.head = None
			print("Last node of the list has been removed. List is empty now!!!")
		else:
			temp = self.head
			self.head = self.head.next # Moved head to the next element
			self.head.prev = None # Setting prev of newly became first node to null
			temp.next = None # Not necesary but still breaking the link of the node that has been removed
			print("Node has been removed")

	#removes the element at the end of the list
	def remove_at_the_end(self):
		if self.head is None:
			print("List is empty, nothing to remove.")
		elif self.head.next == None: # There is only one element in the list
			temp = self.head
			self.head = None
			print("Last node of the list has been removed. List is empty now!!!")
		else:
			temp = self.head
			# temp2 = temp.next
			while temp.next != None: # Loop till temp reaches to the last node
				temp = temp.next

			temp.prev.next = None # Setting next part of the second last node to null
			temp.prev = None # Not necesary but still breaking the link of the node that has been removed
			print("Node has been removed")

	#removes the element at the nth position
	def remove_at_nth_position(self, pos):
		if pos == 0:
			print("Invalid postion")
			return
		elif pos == 1: # Remove element from the begining
			self.remove_at_the_begining()
		else:
			current = self.head
			i=1
			while i < pos and current != None:
				current = current.next
				i = i+1
			if current is None:
				print("Invalid position!!!")
			elif current.next is None: # Remove at the end
				self.remove_at_the_end()
			else:
				current.prev.next = current.next
				current.next.prev = current.prev
				current.prev = None # Not necesary but still breaking the link of the node that has been removed
				current.next = None # Not necesary but still breaking the link of the node that has been removed
				print("Node has been removed")


	#reverses a linked list - TO DO - FIX THIS
	# def reverse(self):
	# 	if self.head is None: #linked list is empty
	# 		print("List is empty, nothing to reverse")
	# 		return
	# 	else:
	# 		currentNode = self.head
	# 		prevNode = None
			
	# 		while currentNode != None:
	# 			nextNode = currentNode.next
	# 			currentNode.next = prevNode
	# 			prevNode = currentNode
	# 			currentNode = nextNode
	# 			# print("%s %s %s" % (prevNode.data, currentNode.data, nextNode.data))								

	# 		self.head = prevNode

	#print using recursion
	def print_recursion(self, p):
		if p == None:
			return
		print(p.data)
		self.print_recursion(p.next)

	#print linked list in reverse order using recursion
	def reverse_print_recursion(self, p):
		if p == None:
			return
		self.reverse_print_recursion(p.next)
		print(p.data)

	#reverse a linked list using recursion
	def reverse_using_recursion(self,p): # Not sure why it is not working. Looking into this
		if p.next == None: # break condition for recursion
			self.head = p
			return

		self.reverse_using_recursion(p.next) 
		q = p.next
		q.prev = q.next # added this line to handle doubly link
		q.next = p
		p.next = None

#LINKED LIST CLASS ENDS HERE

mylist = DoublyLinkedList()


# ADD ELEMENT TO THE LINKED LIST
mylist.add_at_the_end(2)
mylist.add_at_the_end(4)
mylist.add_at_the_end(6)
mylist.add_at_the_end(8)
mylist.add_at_the_end(10)

# mylist.add_at_the_begining(4)
# mylist.add_at_the_begining(3)
# mylist.add_at_the_begining(2)
# mylist.add_at_the_begining(1)
# mylist.add_at_the_begining(0)

# mylist.add_at_the_end(4)
# mylist.add_at_the_end(5)
# mylist.add_at_the_end(6)
# mylist.add_at_nth_position(5,3)
# mylist.add_at_nth_position(5,3)
# mylist.add_at_nth_position(12,7)
# mylist.add_at_nth_position(11,6)


# REMOVE ELEMENT FROM THE LINKED LIST
# mylist.remove_at_the_begining()
# mylist.remove_at_the_begining()
# mylist.remove_at_the_begining()
# mylist.remove_at_the_begining()
# mylist.remove_at_the_begining()
# mylist.remove_at_the_begining()

# mylist.remove_at_the_end()
# mylist.remove_at_the_end()
# mylist.remove_at_the_end()
# mylist.remove_at_the_end()
# mylist.remove_at_the_end()
# mylist.remove_at_the_end()
# mylist.remove_at_nth_position(5)
# mylist.remove_at_nth_position(2)
# mylist.remove_at_nth_position(1)


# PRINT ELEMENTS OF A LINKED LIST
# mylist.print()
# mylist.print_recursion(mylist.head)


# REVERSE ELEMENTS OF A LINKED LIST
# mylist.reverse()
# mylist.reverse_using_recursion(mylist.head) # not working
# mylist.reverse_print_recursion(mylist.head)

mylist.print()
print("Reverse print:")
mylist.reverse_print()















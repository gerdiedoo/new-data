#NODE CLASS STARTS HERE
class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, data):
		self.data = data

	def setNext(self, next):
		self.next = next

#NODE CLASS ENDS HERE

#LINKED LIST CLASS STARTS HERE
# ADD: 1. AT THE BEGINING, 2. AT THE END, 3. AT nth POSITION
# DELETE: 1. AT THE BEGINING, 2. AT THE END, 3. AT nth POSITION
# REVERSE: 1. REVERSE USING ITERATIVE METHOD, 2. REVERSE USING RECURSION
# PRINT: 1. SIMPLE PRINT, 2. PRINT USING RECURSION, 3. REVERSE PRINT USING RECURSION 
class LinkedList:
	def __init__(self):
		self.head = None

	#print the linked list
	def print(self):
		if self.head is None:
			print("linked list is empty, nothing to print")
			return

		current = self.head
		while current:
			print(current.data)
			current = current.next

	#add element at the begining
	def add_at_the_begining(self, data):
		node = Node(data)
		if self.head is None: #linked list is empty
			self.head = node
		else:
			node.next = self.head
			self.head = node

		return self.head

	#add element at the end
	def add_at_the_end(self, data):
		node = Node(data)
		if self.head is None: #linked list is empty
			self.head = node
		else:
			current = self.head
			while current.next != None:
				current = current.next
			
			current.next = node

		return self.head
		
	#inserts the element at the nth position
	#pos=0 will be considered invalid position
	#In a linked list of 4 elements, 2, 4, 6, 8 - pos=1 to pos=5 are valid positions,
	#where pos=1 inserts the element at the beginging of the list and pos=5 inserts the element at the end of the list.
	def add_at_nth_position(self, data, pos):
		node = Node(data)
		
		if pos <= 0:
			return "Invalid position, it can not be less than or equal to 0"
			
		elif pos == 1: #insertion at the begining
				return self.add_at_the_begining(data)
		else:
			current = self.head
			i=1
			while i < pos-1 and current != None: #loop till n-1 position
				current = current.next
				i = i+1

			if current is None:
				return "Invalid position, it exceeds the size of the linked list"
			
			node.next = current.next
			current.next = node
			return self.head

	#removes the element at the begining of the list
	def remove_at_the_begining(self):
		if self.head is None:
			return "List is empty, nothing to remove"
		else:
			temp = self.head
			self.head = self.head.next
			return self.head

	#removes the element at the end of the list
	def remove_at_the_end(self):
		if self.head is None:
			return "List is empty, nothing to remove"
		elif self.head.next == None: #there is only one element in the list
			self.head = None
		else:
			temp = self.head
			temp2 = temp.next
			while temp2.next != None:
				temp = temp2
				temp2 = temp2.next

			temp.next = None

		return self.head

	#removes the element at the nth position
	def remove_at_nth_position(self, pos):
		if pos <= 0:
			return "Invalid position, it can not be less than or equal to 0"
		elif pos == 1: #remove element from the begining
			return self.remove_at_the_begining()
		else:
			temp = self.head
			temp2 = temp.next
			i=1
			while i < pos-1 and temp2 != None:
				temp = temp2
				temp2 = temp2.next
				i = i+1
			if temp2 is None:
				return "Invalid position, it exceeds the size of the linked list"

			temp.next = temp2.next

		return self.head

	#reverses a linked list
	def reverse(self):
		if self.head is None: #linked list is empty
			return "List is empty, nothing to reverse"
		else:
			currentNode = self.head
			prevNode = None
			
			while currentNode != None:
				nextNode = currentNode.next
				currentNode.next = prevNode
				prevNode = currentNode
				currentNode = nextNode
				# print("%s %s %s" % (prevNode.data, currentNode.data, nextNode.data))								

			self.head = prevNode
			return self.head

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
	def reverse_using_recursion(self,p):
		if self.head is None: #linked list is empty
			return "List is empty, nothing to reverse"
		if p.next == None:
			self.head = p
			return self.head

		self.reverse_using_recursion(p.next)
		q = p.next
		q.next = p
		p.next = None
		return self.head

#LINKED LIST CLASS ENDS HERE

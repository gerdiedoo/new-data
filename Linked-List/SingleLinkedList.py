'''      IMPLEMENTATION METHOD 1 (most common)
  HEAD                        TAIL
 ________      ________      ________ 
|      | |    |      | |    |      | |
|  a   | |--->|  b   | |--->|  c   | |--->None
|______|_|    |______|_|    |______|_|

Main Methods: isEmpty, addFirst, addLast, removeFirst, removeLast, makeEmpty
'''
# Exception when attempting to access an element from an empty container.
class EmptyLinkedList(Exception):
	pass
	
class SingleLinkedList:
	
  #-------------------------- nested _Node class --------------------------
	class _Node:
		__slots__ = '_element', '_next'            			# streamline memory for faster attribute access, and space savings in memory.

		def __init__(self, element=None, next=None):    # initialize node's fields
			self._element = element                  			# user's element
			self._next = next                        			# next node reference


	#-------------------------- list constructor --------------------------
	def __init__(self):
		#Create empty LinkedList
		self._head = self._tail = None
		self._size = 0
	
	#-------------------------- public accessors --------------------------
	def __len__(self):
		return self._size								#Return the number of elements in the list.

	def isEmpty(self):
		return self._size==0		#Return True if list is empty.

	def addFirst(self, element):			#O(1)
		if self._head==None:
			n=self._Node(element,None)
			self._tail=n
		else:
			n=self._Node(element,self._head)
		self._head=n
		self._size+=1

	def addLast(self, element):				#O(1)
		n=self._Node(element, None)
		if self._tail!=None:
			self._tail._next=n
		else:
			self._head=n
		self._tail=n
		self._size+=1

	def removeFirst(self):		#O(1)
		if self.isEmpty():
			raise EmptyLinkedList()

		e=self._head._element
		if self._head==self._tail:	#1 element
			self._head=self._tail=None
		else:
			self._head=self._head._next
		self._size-=1
		return e
	
	def removeLast(self):			#O(n)
		if self.isEmpty():
			raise EmptyLinkedList()
	
		e=self._tail._element
		if self._head==self._tail:
			self._head=self._tail=None
		
		else:
			temp=self._head
			while temp._next!=self._tail:
				temp=temp._next
			self._tail=temp
			self._tail._next=None
		self._size-=1
		return e

	def makeEmpty(self):
		self._head = self._tail = None
		self._size = 0

	def getContent(self):
		l=[]
		n=self._head
		while n!= None:
			l.append(n._element)
			n=n._next
		return l

"""Python implementation of a Circular Doubly Linked List With Sentinel"""

class Node(object):
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

	def __str__(self):
		return str(self.data)
		
class CDLLwS(object):
	def __init__(self, nodeClass):
		self.nodeClass = nodeClass

		self.sentinel = self.nodeClass(None)
		self.sentinel.next = self.sentinel.prev = self.sentinel

		self.len = 0
		
	def __len__(self):
		return self.len

	def __iter__(self):
		x = self.sentinel.next
		while x != self.sentinel:
			yield x
			x = x.next

	def __getitem__(self, i):
		if not -1 <= i < len(self):
			raise IndexError()
		elif i == 0:
			return self.sentinel.next
		elif i == -1:
			if len(self) > 0:
				return self.sentinel.prev
			else:
				raise IndexError()
		else:
			for j, x in enumerate(self):
				if j == i: return x

	def _insert_node(self, node, nextNode):
		node.prev = nextNode.prev
		node.next = nextNode
		node.prev.next = node
		node.next.prev = node
		self.len += 1

	def insert(self, i, node):
		self._insert_data(
			node,
			self.__getitem__(i, getNode=True) if len(self) > 0 else self.sentinel
		)

	def append(self, node):
		self._insert_node(
			node,
			self.sentinel
		)

	def pop(self, i=-1):
		x = self[i]

		x.prev.next = x.next
		x.next.prev = x.prev
		
		self.len -= 1
		return x

	def find(self, s, propName="data"):
		for x in self:
			if getattr(x, propName) == s:
				return x
		return None

	def __str__(self):
		return str(map(lambda x:x.data, self))
		

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  linkedlist.py
#  
#  Copyright 2016 Sajal Tyagi <sajaltyagi@Sajals-MacBook-Air.local>
#  

class LinkedList:
	class Node:
		def __init__(self,element,point):
			self._ele = element
			self._next = point
		
	def __init__(self):
		self._head = None
		self._size = 0
	
	
	def getData(self):
		temp = self._head
		if temp != None:
			while temp._next != None :
				print(temp._ele)
				temp = temp._next
			print(temp._ele)
	
	def insertAtBegin(self,ele):
		if self._head == None:
			self._head = self.Node(ele, None)
		else:
			temp = self.Node(ele,self._head)
			self._head = temp
		self._size += 1
	
	def insertAtLast(self,ele):
		if self._head == None:
			self._head = self.Node(ele, None)
		else:
			temp = self._head
			while temp._next != None:
				temp = temp._next
			temp._next = self.Node(ele,None)
		self._size += 1		
	
	def deleteAtLast(self):
		ele = 0
		if self._head == None:
			print("Empty list")
		elif self._head._next == None:
			ele = self._head._ele 
			self._head = None
			self._size -= 1
		else:
			temp = self._head
			while temp._next._next != None:
				temp = temp._next
			ele = temp._next._ele
			temp._next = None
			self._size -= 1
		return ele
	
	def deleteAtBegin(self):
		ele = 0
		if self._head == None:
			print("Empty list")
		elif self._head._next == None:
			ele = self._head._ele
			self._head == None
			self._size -= 1
		else:
			temp = self._head
			ele = temp._ele
			self._head = self._head._next
			temp = None
			self._size -= 1
		return ele
		
	def countNode(self):
		return self._size
	
	def insertAfterPosition(self,ele,pos=0):
		if pos <= 0:
			print("Invalid position item added at first.")
			self.insertAtBegin(ele)
		elif pos >= self._size:
			print("Invalid position item added at last.")
			self.insertAtLast(ele)
		else:
			temp = self._head
			for i in range(0,pos - 1,1):
				temp = temp._next
			node = self.Node(ele,temp._next)
			temp._next = node
		self._size += 1
	
	def insertBeforePosition(self,ele,pos=0):
		if pos <= 0:
			print("Invalid position item added at first.")
			self.insertAtBegin(ele)
		elif pos >= self._size:
			print("Invalid position item added at last.")
			self.insertAtLast(ele)
		else:
			temp = self._head
			for i in range(0,pos - 2,1):
				temp = temp._next
			node = self.Node(ele,temp._next)
			temp._next = node
		self._size += 1


ll = LinkedList()
ll.insertAtBegin(23)
ll.insertAtBegin(54)
ll.insertAtLast(764)
ll.insertAtBegin(9284)
ll.insertAfterPosition(12,3)
ll.insertBeforePosition(98,3)
#ll.deleteAtLast()
#ll.deleteAtBegin()
#ll.deleteAtLast()
#ll.deleteAtLast()
ll.getData()
print(ll.countNode())

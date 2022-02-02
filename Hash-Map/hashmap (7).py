# Abdullah Al Mamun
# amamun@u.rochester.edu

from __future__ import division

class hashMap:

	def __init__(self, size):
		self.size = size
		global hashArray
		global count
		count = 0
		hashArray = [None] * size

##http://garage.pimentech.net/libcommonPython_src_python_libcommof.tringhashcode/
	
	#Function to get the hashcode of a string
	def string_hashcode(self,s):
		h = 0
		for c in s:
			h = (31 * h + ord(c)) & 0xFFFFFFFF
		return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

	#Function for getting the size
	def getSize(self):
		return self.size

	#Function for setting the value along with the key
	def set(self,key,value):
		length = self.size
		k = key
		v = value
		tup = (k,v)
		global hashArray
		global count

		h = self.string_hashcode(k)
		if( hashArray[self.hashFun1(h)] == None ):
			hashArray[self.hashFun1(h)] = tup
			count += 1
			return True
		else:
			for i in range(length):
				if( hashArray[self.hashFun2(h,i)] == None ):
					hashArray[self.hashFun2(h,i)] = tup
					count += 1
					return True
				else:
					continue

	#Function for getting the value by providing the key
	def get(self,key):
		length = self.size
		k = key
		h = self.string_hashcode(k)
		if( hashArray[self.hashFun1(h)] != None ):
			if ( hashArray[self.hashFun1(h)][0] == k ):
				return hashArray[self.hashFun1(h)][1]
		else:
			for i in range(length):
				if( hashArray[self.hashFun2(h,i)] != None ):
					if( hashArray[self.hashFun2(h,i)][0] == k ):
						return hashArray[self.hashFun2(h,i)][1]
					else:
						continue
			return None

	#Function for deleting a value by providing the key
	def delete(self,key):
		length = self.size
		k = key
		h = self.string_hashcode(k)
		global count
		if( hashArray[self.hashFun1(h)] != None ):
			if ( hashArray[self.hashFun1(h)][0] == k ):
				temp = hashArray[self.hashFun1(h)][1]
				hashArray[self.hashFun1(h)] = None
				count -= 1
				return temp

		else:
			for i in range(length):
				if( hashArray[self.hashFun2(h,i)] != None ):
					if( hashArray[self.hashFun2(h,i)][0] == k ):
						temp =  hashArray[self.hashFun2(h,i)][1]
						hashArray[self.hashFun2(h,i)] = None
						count -= 1
						return temp

					else:
						continue
			return None

	#Function for printing the HashMap. It only prints the slots that have something stored in it.
	def printMap(self):
		length = self.size
		for i in range(length):
			if (hashArray[i] != None):
				print hashArray[i]
				print ""
			else:
				continue

	#Function for getting the load factor
	def load(self):
		a = self.getCount() / self.size
		return a

	#Function for getting the how many items have been inserted so far
	def getCount(self):
		self.count = count
		return count

	#First Hash function
	def hashFun1(self,num):
		return num % self.size
	#Second Hash Function
	def hashFun2(self,num,i):
		R = 31
		return (self.hashFun1(num) + i*(R-num%R)) % self.size

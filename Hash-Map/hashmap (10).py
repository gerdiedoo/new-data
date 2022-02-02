#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:26:17 2017

@author: lakshya
"""

#Get a hash code of the string
def get_hashcode(string):
    h = 0
    for c in string:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000


#Node class to store key value pairs of the hash map
class Node():
    
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None

    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value
    
    def setKey(self, key):
        self.key = key
    
    def setValue(self, value):
        self.value = value
    
    def set_next(self, node):
        self.next = node
        
    def get_next(self):
        return self.next
    

#Hash Map Implementation of the class 
class HashMap():
    
    def __init__(self, size):
        self.bucket_size = size
        self.bucket = [Node() for i in range(size)]
  
#Set an object to a corressponding key value    
    def set(self, key, value):
        hash_val = get_hashcode(key) % self.bucket_size
        new_node = Node()
        new_node.setKey(key)
        new_node.setValue(value)

#If the bucket is empty insert at top, else create a linked list with the previous values as head of the linked list
        if(self.bucket[hash_val].getKey() == None ):
            self.bucket[hash_val] = new_node
        else:
            current_node = self.bucket[hash_val]
            while(current_node.get_next() != None):
                if(current_node.getKey() == new_node.getKey()):
                    current_node.setValue(new_node.getValue())
                    return True
                current_node = current_node.next
            
            current_node.set_next(new_node)
            return True

#Get the object corresspoding to the key
    def get(self, key):
        hash_val = get_hashcode(key) % self.bucket_size
        node = self.bucket[hash_val]
        
        while(node.getKey() != None):
            if(node.getKey() == key):
                return node.getValue()
            node = node.next
        
        return None
    
    def delete(self, key):
        hash_val = get_hashcode(key) % self.bucket_size
        
        if(self.bucket[hash_val].getKey() == key ):
            self.bucket[hash_val].setKey(None)
            self.bucket[hash_val].setValue(None)
            return True
        else:
            current_node = self.bucket[hash_val]
            while(current_node.get_next() != None):
                tmp_node = current_node.next
                if(tmp_node.getKey() == key):
                    current_node.set_next(tmp_node.next)
                    return True
                current_node = current_node.next
            
            return False
    
#Calculate the load of the HashMap
    def load(self):
        count = 0
        for node in self.bucket:
            if node.getKey() is not None:
                count += 1

        return float(count) / self.bucket_size


#Testing the HashMap against a set of key value pairs and each function of the HashMap
obj = HashMap(20)
obj.set("lakshya", 10) 
obj.set("kpcb" , 20)
obj.set("coding" , 15)

print obj.get("kpcb")

obj.delete("coding")

print obj.load()
            
        

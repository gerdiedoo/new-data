
# Given the global variables, and the address (id) of the object, get the object
def get_by_address(address, global_vars):
    if address == 0:
        return None
    
    return [x for x in global_vars.values() if id(x) == address][0]

# A doubly linked list node
class Node(object):

    # Constructor
    def __init__(self, data):
        self.data = data
        self.address_store = None
    
    # Get address of this Node object
    def get_address(self):
        return id(self)
    
    # Set neighbours of the node
    def set_neighbors(self, prev_node=None, next_node=None):
        local_address = self.get_address()
        
        # Previous node
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()
        
        # Next node 
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()
        
        # Address store is xor of previous address and current address
        self.address_store = prev_address ^ next_address
    
    # Given the previous node and the global variables, get the next node
    def get_next(self, prev_node, global_vars):
        if self.address_store == None:
            raise Exception('set_neighbors not called yet, no next node!')
            
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()
        
        next_address = self.address_store ^ prev_address
        
        return get_by_address(address=next_address, global_vars=global_vars)
    
    def get_prev(self, next_node, global_vars):
        if self.address_store == None:
            raise Exception('set_neighbors not called yet, no next node!')
        
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()
        
        prev_address = self.address_store ^ next_address
        
        return get_by_address(prev_address, global_vars=global_vars)

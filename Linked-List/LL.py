class LL:
    pred = None
    post = None
    data = None

    def __init__(self,data,post,pred):
        self.data = data
        self.post = post

    def remove(self,data):
        if self.pred == None:           #First of the list.
            if self.data == data:           #Match
                if self.post == None:           #Only
                    self.data = None
                    return 0
                                                
                hold = self.post                #More entries
                self.data = self.post.data
                self.post = self.post.post
                del hold
                return 0
            
            elif self.post == None:         #Last and no match
                return -1
            
            else:
                return self.post.remove(data)   #Search rest
    
        else:
            if self.post == None:       #Last of the list.
                if self.data == data:       #Match
                    hold = self
                    temp = self.pred
                    temp.post = None
                    del hold
                    return 0
                else:
                    return -1               #No match
                
            else:                       #More in list
                if self.data == data:       #Match
                    hold = self
                    temp = self.pred
                    temp.post = self.post
                    del hold
                    return 0
                else:
                    return self.post.remove(data)   #No match

    def insert(self,data):
        if data < self.data:
            hold = LL(data,self,None)
            self = hold

        elif self.post == None:
            hold = LL(data,None,self)
            self.post = hold
            
        else:
            self.post.insert(data)

    def contain(self, s):
            if self.data == None:
                print(s)
            else:
                s = s + ", " + str(self.data)
                if self.post == None:
                    print(s)
                else:
                    self.post.contain(s)

    def contains(self):
        if self.post == None:
            if self.data == None:
                print("Empty.")
            else:
                print(self.data)
        else:
            self.post.contain(str(self.data))
        

        
def test():
    base = LL(0,None,None)
    print("contains...")
    base.contains()
    print()

    print("inserting 1...")
    base.insert(1)
    print("contains:")
    base.contains()
    print()
    
    print("inserting 5...")
    base.insert(5)
    print("contains:")
    base.contains()
    print()

    print("removing 1...")
    base.remove(1)
    print("contains:")
    base.contains()
    print()

    print("removing 5...")
    base.remove(5)
    print("contains...")
    base.contains()
    print()

    print("removing 0...")
    base.remove(0)
    print("contains:")
    base.contains()
    print()

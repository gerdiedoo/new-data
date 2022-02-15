class Node:
    def __init__(self,data):
        self.data= data
        self.next= None


class LinkedList:
    def __init__(self):
        self.first=None
        self.last=None

    def printList(self):
        node=self.first

        print""
        print  "              Printing the list..."
        print"              -------------------------"

        llist=[ ]
        while node!=None:
            llist.append(node.data)
            node=node.next
        if llist :
            print "              Linked List  :", llist
        else:
            print "              List is empty !! "

    def add(self, data):
        new_node =Node(data)

        if self.first==None:     
            self.first=new_node

        if self.last !=None:
            self.last.next=new_node
        self.last= new_node

    def size(self):
        current = self.first
        count=0
        while current !=None:
            count=count+1
            current=current.next
        print "              Size of List is : ", count
        print ""

    def search(self,item):
        current = self.first
        search_item=item
        found = False
        count =1
        
        while current != None and not found:
            if int(current.data) == int(search_item):
                found=True
                print "                    SEARCH NODE FOUND AT POSITION : ",count, " !! "
                print ""
            else:
                current=current.next
                count = count+1

        if current==None and found==False:
            print "                    SEARCH NODE ", search_item, " NOT FOUND !! "
            print""


    def remove(self,search):
        current = self.first
        previous=None
        search_item=search
        found = False
        #i=0
        
        while not found:
            if current.data == search_item:
                found=True
            else:
                    previous=current
                    current=current.next
        if previous==None:
            self.last=current.next()
        else:
            previous.next=current.next
            print "              Element deleted"
        



myList = LinkedList()

menu = {}
menu['1']="Add Nodes" 
menu['2']="Search Node"
menu['3']="Delete Node"
menu['4']="Print List"
menu['5']="Exit"

while True:
    options=menu.keys()
    options.sort()
    print""
    print "        MENU"
    print"======================"
    for entry in options: 
      print entry, menu[entry]
    print""
    selection=raw_input("Please Select:")
    print""
    print ""

    if selection =='1':
        print "              Adding Nodes" 
        print"              -----------------------"
        length=input("              Enter the number of nodes you want for your Linked List  :   ")
        for counter  in range(1,length+1) :
            item=raw_input("              Enter the Linked List elements : ")
            myList.add(item)

        myList.printList()
        myList.size( )
    elif selection == '2': 
      print "              Finding Node"
      print "              -----------------------"
      #Search for a node
      searchValue=input("              Enter the Node value to be searched :  ")
      myList.search(searchValue)
    elif selection == '3':
      print "              Deleting Node" 
      #Remove a Node
      delete=raw_input("              Enter the Node value to be deleted:  ")
      myList.remove(delete)
      myList.printList()
      myList.size( )
    elif selection == '4':
        myList.printList()
        myList.size()
    elif selection == '5': 
      break
    else: 
      print "Unknown Option Selected!" 
















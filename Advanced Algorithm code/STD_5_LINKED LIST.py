
class Node:             # Establish a Node class for the connected list's items
    def __init__(self, dataval=None):   # Constructor to initialize the node object with data value
        self.dataval = dataval  
        self.nextval = None  
class SLinkedList:          #create a class for singly linked lists
    def __init__(self): 
        self.headval = None     #set the list's head to None initially

    def listprint(self):            #method to print every item in the list
        printval = self.headval  
        while printval is not None: #Repeat till the list's conclusion
            print(printval.dataval)  #Print the current node's data value
            printval = printval.nextval  
    
    def AtBeginning(self,newdata):  #Add an element at the beginning of the list
        NewNode = Node(newdata)   
    
    def AtEnd(self, newdata):       #method to add a new node at the end of the list
        NewNode = Node(newdata) 
        if self.headval is None:    #make this node the head if the list is empty
            self.headval = NewNode
            return
        last = self.headval  
        while(last.nextval):           #proceed through the list until the final node
            last = last.nextval
        last.nextval = NewNode   
 
    def Insert(self, val_before, newdata): #method to insert a new node after a node with a specific value
        if self.headval is None:        # Print amessage and return if the list is empty.
            print("The list is empty")
            return 
        current = self.headval  
        while current is not None:          # Go through the list
            if current.dataval == val_before:  # Verify whether the node in use is the one you want to put after 
                NewNode = Node(newdata)  
                NewNode.nextval = current.nextval  
                current.nextval = NewNode  
                return
            current = current.nextval   
        print("Node with value", val_before, "not found.")  

# Set up the individually linked list
list = SLinkedList()
#Building the first collection of nodes and connecting them
list.headval = Node("Mon")  # Establish the head node
e2 = Node("Tue") 
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
# Connecting the nodes
list.headval.nextval = e2 
e2.nextval = e3 
e3.nextval = e4
e4.nextval = e5
list.AtEnd("Sun") # Finishing the list with "Sun"
list.Insert("Tue", "Weds")   #Adding "Weds" to the end of "Tue"
list.listprint()   # Print the whole list to view every day of the week 
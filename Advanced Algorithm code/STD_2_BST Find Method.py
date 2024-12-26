#RECURSIVE
class Node:
    def __init__(self, data=None):       #define a class for a binary tree node that has a constructor
        self.data = data		
        self.left = None		
        self.right = None		
class BinaryTree: 
    def __init__(self):		    #define a class for a binary tree that has a constructor
        self.root = None		

    def insert(self, data):		    #specify how a node is added to the binary tree
        if self.root is None:		
            self.root = Node(data)	
        else:
            self._insert(data, self.root)	

    def _insert(self, data, cur_node):      #establish a helper node insertion method
        if data < cur_node.data:  
            if cur_node.left is None:    
                cur_node.left = Node(data) 
            else:
                self._insert(data, cur_node.left)  
        elif data > cur_node.data:  
            if cur_node.right is None: 	       
                cur_node.right = Node(data)  
            else:
                self._insert(data, cur_node.right) 
        else:
            print("Value already present in tree") 

    def display(self, cur_node):            #specify how the binary tree structure will be shown
        lines, _, _, _ = self._display(cur_node)  
        for line in lines: 		      #The loop displays the binary tree structure by iterating through each line in the lines list
            print(line)     

    def _display(self, cur_node):           # method _display, which accepts a cur_node parameter that is a binary tree node
        if cur_node.right is None and cur_node.left is None:  # check whether the current node is a leaf node
            line = '%s' % cur_node.data     	
            width = len(line)		
            height = 1     		
            middle = width // 2		
            return [line], width, height, middle    

        if cur_node.right is None:	            #This line checks if the current node has no right child
            lines, n, p, x = self._display(cur_node.left)	#The left subtree's lines, width, height ,and middle position are all retrieved
            s = '%s' % cur_node.data 
            u = len(s)     
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s   
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines] 
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2	
        
        if cur_node.left is None:	            #This line checks if the current node has no left child
            lines, n, p, x = self._display(cur_node.right)	
            s = '%s' % cur_node.data  
            u = len(s)  
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines] 
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2 
        # Recursively obtain the left and right subtree's width, height, root location, and display strings
        left, n, p, x = self._display(cur_node.left) 
        right, m, q, y = self._display(cur_node.right) 
        s = '%s' % cur_node.data 
        u = len(s) 
        first_line = (x + 1) * ' ' + (n - x - 1) * '' + s + y * '' + (m - y) * ' '  
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' ' 
        if p < q:  
            left += [n * ' '] * (q - p)   
        elif q < p:  
            right += [m * ' '] * (p - q) 
        zipped_lines = zip(left, right) 
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines] 
        return lines, n + m + u, max(p, q) + 2, n + u // 2   


#Recursive approach for BST
    def find_r(self, target):            #method find_r (recursive) contain a  method search the binary tree for a target value
        if self.root:	
            return self._find_r(target, self.root) 	    #method _find_r is called if the tree has a root
        return None		

    def _find_r(self, target, cur_node):     #helper method to find a specific value in the binary search tree
        if cur_node is None:		        # target not found, node absent
            return None
        if cur_node.data == target:	    #compares the current node's data with the target
            return cur_node		

        elif target > cur_node.data and cur_node.right:
           return self._find_r(target, cur_node.right)	    #calls _find_r recursively on the right child
        elif cur_node.left:	
             return self._find_r(target, cur_node.left)	    #calls _find_r recursively on the left child
        return None  
bst = BinaryTree()		# Make a BinaryTree class instance.
bst.insert(4)			# Fill the binary tree with nodes that have different values
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)
bst.display(bst.root)		             #display the binary tree structure
target_value = int(input("Enter the target value you want to find: "))   #gets the target value from the user
result_node = bst.find_r(target_value)       #look through the tree for the desired value
if result_node:
    print(f"Node with value {target_value} found in the tree.") 
else:
    print(f"Node with value {target_value} not found in the tree.")	





#ITERATIVE
class Node:
    def __init__(self, data=None):       
        self.data = data		
        self.left = None		
        self.right = None		
class BinaryTree:
    def __init__(self):		
        self.root = None		

    def insert(self, data):		
        if self.root is None:		
            self.root = Node(data)	
        else:
            self._insert(data, self.root) 	

    def _insert(self, data, cur_node):		
        if data < cur_node.data:  
            if cur_node.left is None:                     
                cur_node.left = Node(data) 
            else:
                self._insert(data, cur_node.left)  
        elif data > cur_node.data:  
            if cur_node.right is None: 	      
                cur_node.right = Node(data)  
            else:
                self._insert(data, cur_node.right)     
        else:
            print("Value already present in tree")

    def display(self, cur_node): 	
        lines, _, _, _ = self._display(cur_node)    	
        for line in lines: 		
            print(line)     

    def _display(self, cur_node): 
        if cur_node.right is None and cur_node.left is None: 
            line = '%s' % cur_node.data     	
            width = len(line)		
            height = 1     		
            middle = width // 2		
            return [line], width, height, middle    

        if cur_node.right is None:	
            lines, n, p, x = self._display(cur_node.left)	
            s = '%s' % cur_node.data 
            u = len(s)     
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s   
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '	
            shifted_lines = [line + u * ' ' for line in lines] 
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2	
        
        if cur_node.left is None:	
            lines, n, p, x = self._display(cur_node.right)	
            s = '%s' % cur_node.data  
            u = len(s)  
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' ' 
            shifted_lines = [u * ' ' + line for line in lines] 
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2 

        left, n, p, x = self._display(cur_node.left) 
        right, m, q, y = self._display(cur_node.right) 
        s = '%s' % cur_node.data 
        u = len(s) 
        first_line = (x + 1) * ' ' + (n - x - 1) * '' + s + y * '' + (m - y) * ' '  
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' ' 
        if p < q:  
            left += [n * ' '] * (q - p)
        elif q < p:  
            right += [m * ' '] * (p - q) 
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines] 
        return lines, n + m + u, max(p, q) + 2, n + u // 2   

# Iterative approach for BST
    def find_i(self, target):	             # specify a procedure for finding a value in a binary tree
        cur_node = self.root		        #begin at the tree's root
        while cur_node:		                #keep looping(iterate) for as long as there's a node to examine currently
            if cur_node.data == target:      #if current node is eqaul to target 
                return cur_node   	
            elif cur_node.data > target:    #if current node is greater than target 
                cur_node = cur_node.left 
            else:   
                cur_node = cur_node.right   # shift to the right child , where large values are expected 
            return None	

bst = BinaryTree()		
bst.insert(4)			
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)
bst.display(bst.root)		
target_value = int(input("Enter the target value you want to find: "))
result_node = bst.find_i(target_value) 
if result_node:
    print(f"Node with value {target_value} found in the tree.") 
else:
    print(f"Node with value {target_value} not found in the tree.")	

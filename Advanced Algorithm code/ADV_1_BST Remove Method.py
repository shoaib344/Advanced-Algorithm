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

# Method to Remove BST
    def remove(self, target):       # Procedure for eliminating a node from the binary tree
        if self.root is None:       # If there are no nodes in the tree
            return False  
        elif self.root.data == target:  # If the target is the root node
            if self.root.left is None and self.root.right is None:   # If root is childless  
                self.root = None  
            elif self.root.left and self.root.right is None:    # Should root have only left the child
                self.root = self.root.left          #make the left child the new root
            elif self.root.left is None and self.root.right:   #If root only has the right child
                self.root = self.root.right         #make the right child the new root
            else:
                self._remove(self.root)     #remove the helper method by calling both child
            return True  
        parent = None   
        node = self.root
          
        while node and node.data != target:     #navigate the tree until you find the target or get to the end
            parent = node   #Refresh the parent node
            if target < node.data:  #If the goal is smaller than the node that is now in place
                node = node.left   
            elif target > node.data:  #If the target exceeds the current node
                node = node.right  

        if node is None or node.data != target:   # If the intended target cannot be located
            return False  
        
        elif node.left is None and node.right is None:   # If the target node is childless
            if target < parent.data:  #If the target's data is less than the parent's
                parent.left = None  
            else:
                parent.right = None  # Take out the target node from the right  child 
            return True  	

        elif node.left and node.right is None:  # If the target node only has the left child remaining

            if target < parent.data:  
                parent.left = node.left     #assign the target's left child to the parent's left child
            else:
                parent.right = node.left    #assign the target's left child to the right parent
            return True   
        
        elif node.left is None and node.right: #If the target node only has the right  child
            if target < parent.data:  
                parent.left = node.right    #assign the target's right child to the parent's left
            else:
                parent.right = node.right   #assign the target's right child to the parent's right child
            return True  
        else:  
            self._remove(node)  # calling helper method to remove  both child
            return True    

    def _remove(self, node):   #Use the helper technique to remove a node that includes both child
        del_node_parent = node  #Set the parent of the removed node to zero.
        del_node = node.right  
        
        while del_node.left:  #Locate the right subtree's leftmost node
            del_node_parent = del_node   
            del_node = del_node.left  # Shift on the left
        node.data = del_node.data       #Copy the data from the leftmost node to the node being deleted

        if del_node.right:  # If there is a right child on the leftmost node
            if del_node_parent.data > del_node.data:  # If the node on the left is the leftmost
                del_node_parent.left = del_node.right #  Makes it point directly to the right child
            else:
                del_node_parent.right = del_node.right  # Update the parent's right child
        else:   
            if del_node.data < del_node_parent.data:  
                del_node_parent.left = None  #Take out the node on the left
            else:
                del_node_parent.right = None  #Take out the node on the right
                
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
print("Original tree:")
bst.display(bst.root) 
print("\nTree after removing nodes: 11, 2, 14, 3 and 200.")
# Removing nodes
bst.remove(11)
bst.remove(2)
bst.remove(14)
bst.remove(3)
bst.remove(200)
# Display the tree after removing nodes
bst.display(bst.root)
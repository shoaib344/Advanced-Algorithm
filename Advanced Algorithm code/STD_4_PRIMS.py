import sys   
class Graph(): # Define the Graph class.
    def __init__(self, vertices): 	 # Specify the Graph class's constructor method.
        self.V = vertices  # Initialize the number of vertices
        self.graph = [[0 for column in range(vertices)]   # Set all of the graph's elements to 0 to begin.
                      for row in range(vertices)]

    def printMST(self, parent): # Establish a procedure for printing the smallest spanning tree.
        print("Edge \tWeight")   # Print the MST table heading.
        for i in range(1, self.V):  # Go over the vertices iteratively
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])  # Write the weight of each edge.

    def minKey(self, key, mstSet): # Specify a procedure for determining the key value minimum
        min = sys.maxsize #Set the minimum value to the highest value that can be achieved.
        for v in range(self.V):  # Go over each vertex once.
            if key[v] < min and mstSet[v] == False:  # Verify that the vertex is not already in the MST and 
                                                     #that the key value is less than the minimum.
                min = key[v]    # Modify the minimum amount
                min_index = v    # Modify the minimum key's index.
        return min_index  # Give back the minimal key's index.

    def primMST(self): # Using Prim's algorithm, define a procedure for determining the minimal spanning tree.
            key = [sys.maxsize] * self.V    # Create an array with a maximum value at the beginning to store key values.
            parent = [None] * self.V   # Create an array at start to hold the parent node of each vertex.
            key[0] = 0 # Assign 0 as the first vertex's key value.
            mstSet = [False] * self.V   # Initialise an array to record the vertices that are part of the MST
            parent[0] = -1   # Assign -1 to the first vertex's parent.

            for vertex in range(self.V):  # Go over each vertex iteratively.
                u = self.minKey(key, mstSet)  # Locate the vertex with the lowest key value.
                mstSet[u] = True  # Add the chosen vertex to the MST.
                for v in range(self.V):   # Go over each vertex iteratively.      
            
                    
                    if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: # Verify that there is an edge between u and v, that v is not yet in MST, and that 
                                                                                                  # the weight 	of u-v is less than the key value that v now has.
                        key[v] = self.graph[u][v]  # Modify the primary value
                        parent[v] = u  # Vertex v's parent should be updated.
                        
                        
            self.printMST(parent)  # Print the assembled MST.

g = Graph(5)   #Make a graph with five vertices.
                # Establish the graph's adjacency matrix
g.graph = [[0, 2, 0, 6, 0], 
[2, 0, 3, 8, 5],
[0, 3, 0, 0, 7],
[6, 8, 0, 0, 9],
[0, 5, 7, 9, 0]]
g.primMST();  #Utilising Prim's technique, determine and display the smallest spanning tree.

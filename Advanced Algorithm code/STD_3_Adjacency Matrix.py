class Graph:                                      
    def __init__(self, size):           #Initialise the graph with a specified size using the constructor method  
        self.adjMatrix = [] 			#Initialise a blank adjacency matrix
        self.numVertices = size		
        for _ in range(size):	           #loop to produce a zero-filled, empty adjacency matrix
            self.adjMatrix.append([0] * size) 		

    def addVertex(self):            #method to add a vertex to the graph
        self.numVertices += 1
        for row in self.adjMatrix:
            row.append(0)	
        self.adjMatrix.append([0] * self.numVertices) 

    def addEdge(self, i, j):        #method to add an edge to the graph (undirected)
        if 0 < i <= self.numVertices and 0 < j <= self.numVertices:
	        #Indicates a bidirectional link by setting the matrix values for [i][j] and [j][i] to 1
            self.adjMatrix[i-1][j-1] = 1
            self.adjMatrix[j-1][i-1] = 1  

    def removeEdge(self, i, j):    # method to remove an edge from the graph
        #Vertex indices I and J should first be verified to be legitimate, meaning they should be present in the graph
        if 0 < i <= self.numVertices and 0 < j <= self.numVertices:
            # Removes the connection by setting the matrix value for [i][j] and [j][i] to 0
            self.adjMatrix[i-1][j-1] = 0
            self.adjMatrix[j-1][i-1] = 0  

    def printGraph(self):            #method to print the graph as a matrix
        print("    ", end="")         #prints the matrix's header row. Column numbers and spaces are present in this row
        for i in range(1, self.numVertices + 1): # Each column number is printed as iterates from 1 to numVertices (inclusive)
            print(f"{i}   ", end="")
        print("\n")
	
        for i in range(self.numVertices):            # Goes through every graph vertex one by one
            print(f"{i + 1} |  ", end="")
            for j in range(self.numVertices):       #To print the values of the adjacency matrix, go through each vertex again
                print(f"{self.adjMatrix[i][j]}   ", end="")         # Output the value of the adjacency matrix for the vertex-to-vertice (i–j) relationship
            print()

if __name__ == "__main__": 
   
    g = Graph(5)    # Initialize the graph with vertices
    # Adding some edges
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(3, 4)
    g.addEdge(2, 3)
    g.addEdge(1, 6)
    g.addEdge(4, 5)
    # Add a new vertex
    g.addVertex()
    # Removing specified edges
    g.removeEdge(1, 6)
    g.removeEdge(4, 5)
    print ("Final output after removing edges is as follow:")  # Printing the graph after removing edges 
    g.printGraph() 

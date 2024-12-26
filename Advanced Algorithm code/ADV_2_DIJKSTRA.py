from collections import defaultdict 	
import sys	

class Graph():                                         #create the Graph class
    def __init__(self, size):                          #size-parameter-equipped constructor 
        self.edges = defaultdict(list)                 #dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}            
        self.weights = {}                              #dictionary of edges and weights e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}            
        self.size = size
        self.dist = []
        for i in range(size):
            self.dist.append(sys.maxsize)
        self.previous = []
        for i in range(size):
            self.previous.append(None)     
    
    def add_edge(self, from_node, to_node, weight):     #method for adding an edge  
        self.edges[from_node].append(to_node)           
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    def findSmallestNode(self):                         #method to identify the node in Q with the smallest distance
        smallest = self.dist[self.getIndex(self.Q[0])]
        result = self.getIndex(self.Q[0])
        for i in range(len(self.dist)):                 # lterating through Q and finding the vertex with the smallest distance
            if self.dist[i] < smallest:                 # if  smaller distance is found
                node = self.unpoppedQ[i]
                if node in self.Q:                      # if it's already in Q
                    smallest = self.dist[i]
                    result = self.getIndex(node)
        return result       

    def getIndex(self, neighbour):              #method to get the index of a given vertex
        for i in range(len(self.unpoppedQ)):     #  Loop through unpopped queue and find the element
            if neighbour == self.unpoppedQ[i]:   # If the element is equal to what we are looking for
                return i

    def getPopPosition(self, uNode):            #method to push a node into the queue and update its position 
        result = 0
        for i in range(len(self.Q)):            #loop  through popped queue and look for the element
            if self.Q[i] == uNode:
                return i
        return result

    def getUnvisitedNodes(self, uNode):         #method to find all unvisited neighbours of a given node
        resultList = []
        allNeighbours = self.edges[uNode]
        for neighbour in allNeighbours:         #loop through all neighbours
            if neighbour in self.Q:
                resultList.append(neighbour)
        return resultList          

    def dijkstra(self, start, end):          #the application of Dijkstra's algorithm                
        self.Q = []
        for key in self.edges:              
            self.Q.append(key)
        for i in range(len(self.Q)):
            if self.Q[i] == start:
                self.dist[i] = 0
        self.unpoppedQ = self.Q[0:]               

        while self.Q:                               #main loop to find the shortest path                        
            u = self.findSmallestNode()                                     
            if self.dist[u] == sys.maxsize:
                break                                           
            if self.unpoppedQ[u] == end:
                break
            uNode = self.unpoppedQ[u]
            self.Q.remove(uNode)                #remove from unpopped list       
            neighbors = self.getUnvisitedNodes(uNode)       #explore neighbors of the current node
            for neighbor in neighbors:                      #add the distance to each neighbor
                new_distance = self.dist[self.getIndex(uNode)] + self.weights[(uNode, neighbor)]    #new distance to this neighbor is old dist plus weight
                if new_distance < self.dist[self.getIndex(neighbor)]:               #if the new path is shorter, update the distance and previous node
                    self.dist[self.getIndex(neighbor)] = new_distance
                    self.previous[self.getIndex(neighbor)] = uNode

        shortest_path = []      #create the list of shortest paths
        shortest_path.insert(0, end)
        u = self.getIndex(end)                                                  
        while self.previous[u] != None:        # backtrack to build the shortest path
            shortest_path.insert(0, self.previous[u])       #place the node at the path's start                        
            u = self.getIndex(self.previous[u])  
        total_cost = self.dist[self.getIndex(end)]       #calculating total cost

        return shortest_path, total_cost        #returning both shortest path and total cost

graph = Graph(8)

edges = [
    ('O', 'A', 2),
    ('O', 'B', 5),
    ('O', 'C', 4),
    ('A', 'B', 2),
    ('A', 'D', 7),
    ('A', 'F', 12),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('B', 'E', 3),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'T', 5),
    ('E', 'T', 7),
    ('F', 'T', 3),
]
    

for edge in edges:                              #include every edge in the graph
    graph.add_edge(*edge)
path, cost = graph.dijkstra('O', 'T')            #run Dijkstra's algorithm from 'O' to 'T'
print(f"Shortest path: {path} , with total cost: {cost}")       #output the shortest path and total cost
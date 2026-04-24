# DFS - depth first search
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] =1
        self.adjMatrix[v2][v1] =1
    def removeEdge(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return 
        self.adjMatrix[v1][v2]= 0
        self.adjMatrix[v2][v1]= 0
    # dfs helper function  
    # sv indicates starting vertex
    def __dfsHelper(self,sv,visited):
        
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]>0 and visited[i] is False:
                self.__dfsHelper(i,visited)

    # dfs function
    def dfs(self):
        # visited indicated the visited vertex so we are maintaining a visited array so that it should visit again
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i,visited)
    def containEdge(self,v1,v2):    
        if self.adjMatrix[v1][v2]>0 :
            return True
        else:
            return False      
    def __str__(self):
        return str(self.adjMatrix) 

g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,3)
g.addEdge(0,2)
g.dfs()
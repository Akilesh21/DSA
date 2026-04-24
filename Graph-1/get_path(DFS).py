


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1, v2) is False :
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else: 
            return False
        
    def __str__(self):
        return str(self.adajMatrix)
    
        
               
       
    def __getPathDFS(self, sv, ev, visited) :
        if sv == ev :
            return list([sv])
        
        visited[sv] = True
    
        for i in range(self.nVertices) :
            if self.adjMatrix[sv][i] == 1 and not visited[i] :
                li = self.__getPathDFS(i, ev, visited)
                
                if li != None :
                    li.append(sv)
                    return li
        
        return None
    
 
    
    def getPathDFS(self, sv, ev) :
        visited = [False for i in range(self.nVertices)]
        return self.__getPathDFS(sv, ev, visited)   



# MainS
g = Graph(5)       
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(0,2)
print(g.getPathDFS(0,3))
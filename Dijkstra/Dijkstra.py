import sys 
   
class Graph(): 
   
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def minDistance(self, dist, sptSet): 
   
        min = sys.maxsize 
   
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v]
                min_index = v 
   
        return min_index 
   
    def dijkstra(self, src): 
   
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v]
        for node in range(self.V): 
            print ("Кратчайший путь от 1 вершины до", end=" ")
            print (node+1, " = ", dist[node]) 
   
g = Graph(7) # количество вершин
g.graph = [                      # матрица смежности
    [0,7,3,0,0,8,0],
    [0,0,0,8,0,0,0],
    [0,0,0,2,4,0,0],
    [0,0,0,0,0,0,5],
    [0,0,0,0,0,0,6],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0]
    ]   
g.dijkstra(0); 

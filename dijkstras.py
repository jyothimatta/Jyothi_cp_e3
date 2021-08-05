# Write a program that finds the shortest path from a source 
# vertex (0) to all other vertices. Following is a sample 
# input and output files.

# Sample Input:
# 8
# 15
# 4 5 0.35
# 5 4 0.35
# 4 7 0.37
# 5 7 0.28
# 7 5 0.28
# 5 1 0.32
# 0 4 0.38
# 0 2 0.26
# 7 3 0.39
# 1 3 0.29
# 2 7 0.34
# 6 2 0.40
# 3 6 0.52
# 6 0 0.58
# 6 4 0.93

# Sample Output:
#  0 to 0 (0.00)  
#  0 to 1 (1.05)  0->4  0.38   4->5  0.35   5->1  0.32
#  0 to 2 (0.26)  0->2  0.26
#  0 to 3 (0.99)  0->2  0.26   2->7  0.34   7->3  0.39
#  0 to 4 (0.38)  0->4  0.38
#  0 to 5 (0.73)  0->4  0.38   4->5  0.35
#  0 to 6 (1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52
#  0 to 7 (0.60)  0->2  0.26   2->7  0.34

import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        for node in range(self.V):
            print(node, "t", dist[node])
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
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
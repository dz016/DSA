
from collections import deque
class Graph:
    def __init__(self,V=0,edges=[], isDirected=False) -> None:
        self.adjList = [[] for i in range(V)]

        for i,ele in enumerate(edges):
            self.adjList[ele[0]].append(ele[1])
            if not isDirected:
                self.adjList[ele[1]].append(ele[0])

    def BFS(self,src =0):
        visited = [False for i in self.adjList]
        ans=[]
        Q= deque()
        Q.append((src,0))
        while Q:
            front_value = Q.popleft()

            ans.append(front_value)
            for  neighbor in self.adjList[front_value[0]]:
               if not visited[neighbor]:
                   Q.append((neighbor,front_value[1] +1))
                   visited[neighbor]= True
        return ans
    def DFS(self,src=0):

        visited= [ False for i in self.adjList]
        ans = []

        def dfs(i):
            ans.append(i)
            visited[i] = True
            for ele in self.adjList[i]:
                if not visited[ele]:
                    dfs(ele)
        dfs(src)
        return ans

    def cycle_dfs_undirected(self):

        visited = [False for i in  self.adjList]
        def dfs(curr, prev):
            visited[curr]= True
            for neighbour in self.adjList[curr]:
                if not visited[neighbour]:
                    if dfs(neighbour,curr):
                        return True
                elif neighbour != prev:
                    return True
            return False

        return dfs(0,-1)

    def cycle_bfs_undirected(self):
        visited = [False for i in  self.adjList]
        Q= deque()
        Q.append((0,-1))
        while Q:
            front_value=Q.popleft()
            current= front_value[0]
            came_from = front_value[1]
            for neighbour in self.adjList[current]:
                if not visited[neighbour]:
                    Q.append((neighbour,current))
                    visited[neighbour]= True
                elif neighbour != came_from:
                    return True
        return False


    def cycle_dfs_directed(self):
        visited =[False for i in self.adjList]
        onPath =[False for i in self.adjList]

        def dfs(i):
            visited[i]=True
            onPath[i]=True
            for neighbour in self.adjList[i]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True

                elif onPath[neighbour]:
                    return True

            onPath[i]=False
            return False

        for i,ele in enumerate(visited):
            if not ele:
                if dfs(i):
                    return True
        return False














# # Test Case 1: Directed Graph
# #cyclic
V = 4
edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
isDirected = True

graph = Graph(V, edges, isDirected)
print("adjList:",graph.adjList,end="\n")  # Expected Output: [[1], [2], [0,3]]
print("BFS taraversal:", graph.BFS(),end="\n")
print("DFS taraversal:", graph.DFS(),end="\n")
print("Is there cycle?(dfs) ->:", graph.cycle_dfs_directed(),end="\n")

# non-cyclic
V = 4
edges = [(0, 1), (1, 2), (2, 3)]
isDirected = True

graph = Graph(V, edges, isDirected)
print("adjList:",graph.adjList,end="\n")  # Expected Output: [[1], [2], [0,3]]
print("BFS taraversal:", graph.BFS(),end="\n")
print("DFS taraversal:", graph.DFS(),end="\n")
print("Is there cycle?(dfs) ->:", graph.cycle_dfs_directed(),end="\n")






# Test Case 2: Undirected Graph
# non-cyclic
# V = 5
# edges = [(0, 1), (1, 2), (1, 3), (3, 4)]  # No cycle, simple tree structure
# isDirected = False

# graph = Graph(V, edges, isDirected)
# print("adjList:",graph.adjList,end="\n")  # Expected Output: [[1], [2], [0,3]]
# print("BFS taraversal:", graph.BFS(),end="\n")
# print("DFS taraversal:", graph.DFS(),end="\n")
# print("Is there cycle?(dfs) ->:", graph.cycle_dfs_undirected(),end="\n") # Expected Output: [[1], [0, 2, 3], [1], [1, 4], [3]]
# print("Is there cycle?(bfs) ->:", graph.cycle_bfs_undirected(),end="\n")
# # cyclic
# V = 5
# edges = [(0, 1), (1, 2), (1, 3),(2,3), (3, 4)]  # No cycle, simple tree structure
# isDirected = False

# graph = Graph(V, edges, isDirected)
# print("adjList:",graph.adjList,end="\n")  # Expected Output: [[1], [2], [0,3]]
# print("BFS taraversal:", graph.BFS(),end="\n")
# print("DFS taraversal:", graph.DFS(),end="\n")
# print("Is there cycle?(dfs) ->:", graph.cycle_dfs_undirected(),end="\n")
# print("Is there cycle?(bfs) ->:", graph.cycle_bfs_undirected(),end="\n")

# #Test Case 3: DAG
# V=6
# edges=[(5,2),(5,0),(4,1),(4,0),(2,3),(3,1)]
# isDirected=True
# graph = Graph(V, edges, isDirected)
# print(graph.adjList,graph.BFS(),graph.DFS())

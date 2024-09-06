from collections import deque

class Graph:
    def __init__(self, n, edges, isDirected=True) -> None:

        # Create adjacency list
        self.adjList = {i: [] for i in range(n)}  # Initialize an empty list for each node
        for ele in edges:
            self.adjList[ele[0]].append(ele[1])  # Add the edge to the adjacency list
            if not isDirected:
                self.adjList[ele[1]].append(ele[0])  # Add the reverse edge if undirected

        # Create adjacency matrix
        self.adjMat = [[-1 for _ in range(n)] for _ in range(n)]  # Initialize matrix with -1
        for ele in edges:
            self.adjMat[ele[0]][ele[1]] = 1  # Mark the edge in the matrix
            if not isDirected:
                self.adjMat[ele[1]][ele[0]] = 1  # Mark the reverse edge if undirected



    def BFSR(self,val=0):
        visited = {key:False for key in self.adjList}
        queue= deque()
        queue.append(val)

        ans =""
        def _BFS():
            nonlocal ans
            n =len(queue)
            if n != 0:
                for _ in range(n):
                    front_value = queue.popleft()
                    if visited[front_value]:
                        continue
                    else:
                        ans = ans + str(front_value) +" "
                        for ele in self.adjList[front_value]:
                            queue.append(ele)
                        visited[front_value] = True



                _BFS()

            return


        _BFS()
        return ans


    def BFSI(self,val =0):
        visited = [False for _ in self.adjList]
        queue = deque()
        queue.append(val)
        ans = ""

        while queue:
            n = len(queue)

            for i in range(n):
                front_value = queue.popleft()
                if not visited[front_value]:
                    ans =ans + str(front_value) + " "
                    visited[front_value] = True

                    for ele in self.adjList[front_value]:
                        queue.append(ele)
            ans = ans + ","


        return ans

    def printAdjList(self):
        """Prints the adjacency list of the graph."""
        for v, n in self.adjList.items():
            print(f"{v} -> {n}")

    def printAdjMatrix(self):
        """Prints the adjacency matrix of the graph."""
        for row in self.adjMat:
            print(row)


# Test cases to demonstrate the functionality of the Graph class
print("--------Test Graph 1--------")
edges = [(0, 1), (0, 2), (1, 2), (2, 3),(0,4),(1,5),(1,6),(6,7),(6,8),(2,9)]
g1 = Graph(10, edges, False)  # Creating an undirected graph
print("Undirected Graph - Adjacency List:")
g1.printAdjList()  # Should print adjacency list for undirected graph
print(g1.BFSR())
print(g1.BFSI())

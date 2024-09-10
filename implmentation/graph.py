from collections import deque

class Graph:
    def __init__(self, n, edges, isDirected=True) -> None:
        # Create adjacency list
        self.adjList = {i: [] for i in range(n)}
        for ele in edges:
            self.adjList[ele[0]].append(ele[1])
            if not isDirected:
                self.adjList[ele[1]].append(ele[0])

        # Create adjacency matrix
        self.adjMat = [[-1 for _ in range(n)] for _ in range(n)]
        for ele in edges:
            self.adjMat[ele[0]][ele[1]] = 1
            if not isDirected:
                self.adjMat[ele[1]][ele[0]] = 1

    def BFSR(self, val=0):
        visited = {key: False for key in self.adjList}
        ans = ""

        def _BFS(queue):
            nonlocal ans
            if not queue:
                return

            n = len(queue)
            for _ in range(n):
                front_value = queue.popleft()
                if visited[front_value]:
                    continue
                ans += str(front_value) + " "
                visited[front_value] = True
                for ele in self.adjList[front_value]:
                    if not visited[ele]:
                        queue.append(ele)

            _BFS(queue)

        queue = deque([val])
        _BFS(queue)
        return ans.strip()

    def BFSI(self, val=0):
        visited = [False for _ in self.adjList]
        queue = deque([val])
        ans = ""

        while queue:
            n = len(queue)
            for _ in range(n):
                front_value = queue.popleft()
                if not visited[front_value]:
                    ans += str(front_value) + " "
                    visited[front_value] = True
                    for ele in self.adjList[front_value]:
                        if not visited[ele]:
                            queue.append(ele)
            ans = ans.strip() + ","

        return ans.strip(',')

    def DFS(self, start):
        visited = {key: False for key in self.adjList}
        ans = ""

        def _DFS(val):
            if visited[val]:return
            nonlocal ans
            ans += str(val) + " "
            visited[val] = True
            for ele in self.adjList[val]:
                    _DFS(ele)

        _DFS(start)
        return ans.strip()

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
edges = [(0, 1), (0, 2), (1, 2), (2, 3), (0, 4), (1, 5), (1, 6), (6, 7), (6, 8), (2, 9)]
g1 = Graph(10, edges, False)  # Creating an undirected graph
print("Undirected Graph - Adjacency List:")
g1.printAdjList()  # Should print adjacency list for undirected graph
print("BFS Recursive:", g1.BFSR())
print("BFS Iterative:", g1.BFSI())
print("DFS:", g1.DFS(0))

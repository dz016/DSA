class Graph:
    def __init__(self, n, edges, isDirected=True) -> None:
        """
        Initialize the graph.

        Parameters:
        n (int): Number of nodes in the graph.
        edges (list of tuples): List of edges where each edge is represented as a tuple (u, v).
        isDirected (bool): If True, the graph is directed. If False, the graph is undirected.

        Creates:
        - An adjacency list (self.adjList) to store the graph.
        - An adjacency matrix (self.adjMat) to store the graph.
        """
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
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
g1 = Graph(4, edges, False)  # Creating an undirected graph
print("Undirected Graph - Adjacency List:")
g1.printAdjList()  # Should print adjacency list for undirected graph
print("\nUndirected Graph - Adjacency Matrix:")
g1.printAdjMatrix()  # Should print adjacency matrix for undirected graph

print("--------Test Graph 2--------")
g2 = Graph(4, edges, True)  # Creating a directed graph
print("\nDirected Graph - Adjacency List:")
g2.printAdjList()  # Should print adjacency list for directed graph
print("\nDirected Graph - Adjacency Matrix:")
g2.printAdjMatrix()  # Should print adjacency matrix for directed graph

print("--------Test Graph 3--------")
g3 = Graph(4, [], True)  # Creating a graph with no edges
print("\nEmpty Graph - Adjacency List:")
g3.printAdjList()  # Should print an empty adjacency list
print("\nEmpty Graph - Adjacency Matrix:")
g3.printAdjMatrix()  # Should print an adjacency matrix filled with -1

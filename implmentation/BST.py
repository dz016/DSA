from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return "Inserted root"
        return self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = Node(val)
                return "Inserted left"
            else:
                return self._insert(node.left, val)
        elif val > node.val:
            if not node.right:
                node.right = Node(val)
                return "Inserted right"
            else:
                return self._insert(node.right, val)
        else:
            return "Value already exists"

    def display(self):
        self._display(self.root)

    def _display(self, node):
        if not node:
            return
        print(node.val)
        self._display(node.left)
        self._display(node.right)

    def BFS(self):
        queue = deque()
        if not self.root:
            return "Tree is empty"
        queue.append(self.root)
        self._BFS(queue)

    def _BFS(self, queue):
        while queue:
            currNode = queue.popleft()  # Corrected to popleft()
            print(currNode.val, end=" -> ")
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        print("None")  # To indicate end of BFS

# Test cases
def test_bst():
    bst = BST()

    print(bst.insert(10))  # Output: Inserted root
    print(bst.insert(5))   # Output: Inserted left
    print(bst.insert(15))  # Output: Inserted right
    print(bst.insert(3))   # Output: Inserted left
    print(bst.insert(7))   # Output: Inserted right
    print(bst.insert(12))  # Output: Inserted left
    print(bst.insert(18))  # Output: Inserted right
    print(bst.insert(5))   # Output: Value already exists

    print("\nTree display (Pre-Order Traversal):")
    bst.display()  # Should display all nodes in pre-order traversal

    print("\nBFS Traversal:")
    bst.BFS()  # Should display BFS traversal

test_bst()

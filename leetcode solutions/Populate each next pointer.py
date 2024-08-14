"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self) -> :
        self.ans= root
        self.queue = deque()
        if root:
            self.queue.append(root)
            self._connect()
        return self.ans

    def _connect(self):
        pointer =self.queue.popleft() 
        n = len(self.queue)
        if pointer.left:
            self.queue.append(pointer.left)
        if pointer.right:
            self.queue.append(pointer.right)  
        for _ in range(n):
            current = self.queue.popleft()
            pointer.next = current
            pointer = current
            if current.left:
                self.queue.append(current.left)
            if current.right:
                self.queue.append(current.right)
        pointer.next =None
        if len(self.queue) == 0:
            return
        self._connect()











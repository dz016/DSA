# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root) :
        self.ans =[]
        self.queue = deque()
        if root:
            self.queue.append(root)
            self._rightSideView()
        return self.ans
    def _rightSideView(self):
        n = len(self.queue)
        if n==0:
            return
        for _ in range(n-1):
            current = self.queue.popleft()
            if current.left:
                self.queue.append(current.left)
            if current.right:
                self.queue.append(current.right)
        current = self.queue.popleft()
        if current.left:
            self.queue.append(current.left)
        if current.right:
            self.queue.append(current.right)
        self.ans.append(current.val)
        self._rightSideView()









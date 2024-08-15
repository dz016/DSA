# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.ans = False
        self.queue = deque()
        if root:
            self.queue.append(root)
            self._isCousins(x,y)
        return self.ans


    def _isCousins(self,x,y):
        n = len(self.queue)
        utils = {}
        for i in range(n):
            current = self.queue.popleft()
            if not current:
                continue
            if current.val == x or current.val == y:
                utils[current.val] = i
            self.queue.append(current.left)
            self.queue.append(current.right)
        if x in utils and y in utils and (min(utils[x],utils[y])%2 !=0 if abs(utils[x]-utils[y]) == 1 else True) :
            self.ans = True
            return
        if len(self.queue) ==0:
            return
        self._isCousins(x,y)









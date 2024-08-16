# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            self.ans = True
            self.queue = deque()
            if root:
                self.queue.append(root)
                self._isSymmetric()
            return self.ans

        def isPalindrome(self, Que):
            isPalindrome = True
            i = 0
            j = len(Que) - 1
            while i <= j:


                if (Que[i].val==Que[j].val if Que[i] !=None and Que[j]!=None else  Que[i] == Que[j]):
                    i = i + 1
                    j = j - 1
                else:
                    isPalindrome = False
                    break
            return isPalindrome

        def _isSymmetric(self):

            if not self.isPalindrome(self.queue):

                self.ans = False
                return

            n = len(self.queue)

            for _ in range(n):
                current = self.queue.popleft()
                if not current:
                    continue
                self.queue.append(current.left)
                self.queue.append(current.right)

            if len(self.queue) == 0:
                return
            self._isSymmetric()

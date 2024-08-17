# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        ans = self._maxDepth(root)
        return ans



    def _maxDepth(self,node):
        if node is None:
            return 0
        leftMaxDepth = self._maxDepth(node.left)
        rightMaxDepth = self._maxDepth(node.right)
        return max(   leftMaxDepth,rightMaxDepth)+1

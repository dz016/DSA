# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self._kthSmallest(root,k)
        return self.ans


    def _kthSmallest(self, node,k):
        if node is None:
            return
        self._kthSmallest(node.left,k)
        self.count = self.count +1

        if self.count == k:
            self.ans = node.val

        self._kthSmallest(node.right,k)






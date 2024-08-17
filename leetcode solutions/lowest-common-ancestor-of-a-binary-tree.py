# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = root
        self._lowestCommonAncestor(root,p,q)
        return self.ans


    def _lowestCommonAncestor(self, root, p, q):
        if root is None:
            return False
        if root == p or root == q:
            self.ans = root
            return True


        left = self._lowestCommonAncestor(root.left,p,q)
        right = self._lowestCommonAncestor(root.right,p,q)
        if left and right:
            self.ans = root
            return False
        return left or right


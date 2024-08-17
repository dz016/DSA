# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right
        if root.left is None:
            return
        root.right = root.left
        pointer = root
        root.left =None

        while pointer.right:
            pointer = pointer.right
        pointer.right = right


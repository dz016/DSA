# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self._diameterOfBinaryTree(root)
        return self.ans
    def _diameterOfBinaryTree(self,node):
        if node is None:
            return 0
        leftHeight = self._diameterOfBinaryTree(node.left)
        rightHeight = self._diameterOfBinaryTree(node.right)
        if (leftHeight + rightHeight >self.ans):
            self.ans = leftHeight + rightHeight
        return max(leftHeight ,rightHeight)+1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        low = float("-inf")
        high = float("inf")
        self._isValidBST(root,low,high)
        return self.ans



    def _isValidBST(self, node ,low ,high):
        if node is None:
            return
        if low<node.val<high:
            self._isValidBST(node.left ,low,node.val)
            self._isValidBST(node.right ,node.val,high)
        else:
            self.ans = False
            return



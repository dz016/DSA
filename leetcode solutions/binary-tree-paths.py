# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [f"{root.val}"]

        left = self.binaryTreePaths(root.left)
        right =  self.binaryTreePaths(root.right)
        res = left + right
        for i in range(len(res)):
            res[i] = f"{root.val}->" + res[i]
        return res


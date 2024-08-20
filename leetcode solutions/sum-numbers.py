# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper( root,num):

            if root is None:
                return 0
            ans = root.val  + num *10

            if root.left is None and root.right is None:
                return ans
            left = helper(root.left,ans)
            right = helper(root.right,ans)
            return left + right
        return helper(root,0)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = root.val
        def helper(root):
            nonlocal answer
            if root is None:
                return 0



            left = helper(root.left)
            right = helper(root.right)
            left = max(0,left)
            right = max(0,right)

            if left + root.val + right > answer:
                answer = left + root.val + right
            return max(left + root.val , right+root.val)
        helper(root)
        return answer


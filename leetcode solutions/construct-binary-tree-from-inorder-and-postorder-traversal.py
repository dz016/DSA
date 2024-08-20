# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) ==0:
            return None
        node = TreeNode(postorder[-1])
        index =0
        for i in range(len(inorder)):
            if node.val == inorder[i]:
                index =i
                break

        arr = inorder[index +1 : ]
        node.left = self.buildTree(inorder[:index] ,postorder[:-len(arr)-1 ])
        node.right = self.buildTree(arr ,postorder[-len(arr)-1 : -1])
        return node

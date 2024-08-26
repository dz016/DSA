

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans =[]
        def hpostorder(node):
            if node is None:
                return
            for i in range(len(node.children)):
                hpostorder(node.children[i])
            ans.append(node.val)
        hpostorder(root)
        return ans

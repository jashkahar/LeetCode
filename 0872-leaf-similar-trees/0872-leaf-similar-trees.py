# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
                
        def findleaf(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            findleaf(root.left, leaf)
            findleaf(root.right, leaf)
            
        leaf1 = []
        leaf2 = []
        
        findleaf(root1, leaf1)
        findleaf(root2, leaf2)
        
        return leaf1 == leaf2
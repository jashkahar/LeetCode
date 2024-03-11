# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.zigzag(root.left, True, 0), self.zigzag(root.right, False, 0))
        
    def zigzag(self, root, isleft, depth):
            if not root:
                return depth
            
            if isleft:
                depth = max(depth, self.zigzag(root.right, False, depth + 1), self.zigzag(root.left, True, 0))
            else:
                depth = max(depth, self.zigzag(root.left, True, depth + 1), self.zigzag(root.right, False, 0))
            return depth
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        q = [root]
        maxlevel = 1
        level = 1
        maxsum = float('-inf')
        
        while q:
            levelsum = 0
            nextlevel = []
            
            for node in q:
                levelsum += node.val
    
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
                    
            if levelsum > maxsum:
                maxsum = levelsum
                maxlevel = level
            q = nextlevel
            level += 1
        return maxlevel
                
        
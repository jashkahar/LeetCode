# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1
            
        def dfs(node, rootsum):
            if not node:
                return
            rootsum +=node.val
            self.total += self.lookup[rootsum]
            self.lookup[rootsum + targetSum] +=1
            dfs(node.left, rootsum)
            dfs(node.right, rootsum)
            self.lookup[rootsum+targetSum] -=1
            
        dfs(root,0)
        
        return self.total
        
#         self.total = 0
        
#         def helper(node, cur):
#             if not node:
#                 return
#             helper(node.left, cur+node.val)
#             helper(node.right, cur+node.val)
#             # print(cur +node.val)
#             if cur + node.val == targetSum:
#                 self.total += 1
#                 # print('hello')
            
#         def dfs(node):
#             # print('hi')
#             if not node:
#                 return
#             helper(node, 0)
#             dfs(node.left)
#             dfs(node.right)
            
#         dfs(root)
        
#         return self.total
        
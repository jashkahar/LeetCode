# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []
        
        queue = deque()
        avg =[]
        queue.append(root)

        while queue:
            qLen = len(queue)
            curSum = 0
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    curSum += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            avg.append(curSum/qLen)

        return avg


        
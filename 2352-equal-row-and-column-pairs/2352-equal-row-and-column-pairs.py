import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = defaultdict(int)
        
        c = 0
        
        for row in grid:
            row_counts[tuple(row)] += 1
        for columns in zip(*grid):
            c += row_counts[columns]
        return c
        
#         print(grid)
#         tgrid = np.transpose(grid)
#         tgrid = tgrid.tolist()
#         print(tgrid)
#         c1=0
#         for row in grid:
#             if row in tgrid:
#                 c1 += 1
#         c2 = 0
#         for row in tgrid:
#             if row in grid:
#                 c2 += 1
#         return c1+c2
                
    
    
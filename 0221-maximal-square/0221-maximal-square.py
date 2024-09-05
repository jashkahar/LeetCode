class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols =len(matrix), len(matrix[0])
        cur_max = 0
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if matrix[r][c] == "0":
                    continue
                else:
                    if r+1 >= rows or c+1 >= cols:
                        matrix[r][c] = 1
                    else:
                        matrix[r][c] = (1 + min(int(matrix[r+1][c]),
                                                int(matrix[r+1][c+1]),
                                                int(matrix[r][c+1])))
                cur_max = max(cur_max, matrix[r][c])
        return cur_max**2
        

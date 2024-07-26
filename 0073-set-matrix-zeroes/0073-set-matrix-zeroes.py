class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row, cols = len(matrix), len(matrix[0])
        rowZero = False
        
        for r in range(row):
            for c in range(cols):
                if matrix [r][c] == 0:
                    matrix[0][c] = 0
                    if r>0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, row):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def countNeighbours(r, c):
            nei = 0
            
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i >= rows or j >= cols):
                        continue
                    if board[i][j] in [1, -1]:
                        nei += 1
            return nei
        
        for r in range(rows):
            for c in range(cols):
                nei = countNeighbours(r, c)
                
                if board[r][c] == 1 and (nei < 2 or nei > 3):
                    board[r][c] = -1  # Live to dead
                elif board[r][c] == 0 and nei == 3:
                    board[r][c] = 2   # Dead to live
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0  # Convert marked dead cells
                elif board[r][c] == 2:
                    board[r][c] = 1  # Convert marked live cells


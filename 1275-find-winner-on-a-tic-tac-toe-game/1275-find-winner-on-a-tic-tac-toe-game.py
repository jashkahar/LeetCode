class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        row = [0] * n
        col = [0] * n
        diag1 = 0
        diag2 = 0

        player = 1

        for i,j in moves:

            row[i] += player
            col[j] += player
            if i == j:
                diag1 += player
            if i+j == n-1:
                diag2 += player
            
            if abs(row[i]) == n or abs(col[j]) == n or abs(diag1) == n or abs(diag2) == n:
                if player == 1:
                    return "A"
                else:
                    return "B"
            player *= -1
        if len(moves) == (n*n):
            return "Draw"
        else:
            return "Pending"

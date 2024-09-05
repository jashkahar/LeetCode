class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0] * len(obstacleGrid[0])

        dp[-1] = 1

        for i in range(len(obstacleGrid) - 1 , -1, -1):
            for j in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j + 1 < len(obstacleGrid[0]):
                    dp[j] = dp[j] + dp[j+1]
        return dp[0]

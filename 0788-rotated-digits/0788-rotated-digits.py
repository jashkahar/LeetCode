class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [0] * (n + 1)
        count = 0
        
        for i in range(1, n + 1):
            if i < 10:
                if i in [0, 1, 8]:
                    dp[i] = 0  # Valid but unchanged when rotated
                elif i in [2, 5, 6, 9]:
                    dp[i] = 1  # Valid and changes when rotated
                    count += 1
                else:
                    dp[i] = -1
            else:
                # Combine the results of the last digit and the rest of the number
                digit1 = dp[i % 10]  # Last digit
                digit2 = dp[i // 10]  # Rest of the number
                
                if digit1 == -1 or digit2 == -1:
                    dp[i] = -1  # Invalid if any part is invalid
                elif digit1 == 1 or digit2 == 1:
                    dp[i] = 1  # Valid and changes when rotated
                    count += 1
                else:
                    dp[i] = 0  # Valid but unchanged when rotated
        
        return count

            

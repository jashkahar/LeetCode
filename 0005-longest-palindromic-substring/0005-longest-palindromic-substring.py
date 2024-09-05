class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        max_len = 1
        start_index = 0

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start_index = i
                max_len = 2
        
        for cur_len in range(3, n+1):
            for start in range(n - cur_len + 1):
                end = start + cur_len - 1

                if dp[start + 1][end - 1] and s[start] == s[end]:
                    dp[start][end] = True

                    if cur_len > max_len:
                        start_index = start
                        max_len = cur_len
        return s[start_index : start_index + max_len]
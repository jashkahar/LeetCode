class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        prefix_sum = [0] * n
        candle_left = [0] * n
        candle_right = [0] * n

        prefix_sum[0] = 1 if s[0] == "*" else 0
        candle_left[0] = 1 if s[0] == "|" else 0
        candle_right[n-1] = 1 if s[n-1] == "|" else n

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + 1 if s[i] == "*" else prefix_sum[i-1]
            candle_left[i] = i if s[i] == "|" else candle_left[i-1]
        
        for i in range(n-2, -1, -1):
            candle_right[i] = i if s[i] == "|" else candle_right[i+1]
        
        res = []

        for i in range(len(queries)):
            start = candle_right[queries[i][0]]
            end = candle_left[queries[i][1]]
            res.append(0 if start >= end else prefix_sum[end] - prefix_sum[start])
        return res





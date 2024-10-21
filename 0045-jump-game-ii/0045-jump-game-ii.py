class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        
        return dp[-1]
        # res = 0
        
        # l,r = 0,0
        
        # while r<len(nums)-1:
        #     farthest = 0
        #     for i in range(l, r+1):
        #         farthest  = max(farthest, i+nums[i])
        #     l = r+1
        #     r = farthest
        #     res += 1
        # return res
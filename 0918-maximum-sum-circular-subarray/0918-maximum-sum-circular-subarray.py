class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gloMax, gloMin = nums[0], nums[0]
        curMax, curMin = 0,0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            gloMax = max(gloMax, curMax)
            gloMin = min(gloMin, curMin)

        return max(gloMax, total - gloMin) if gloMax > 0  else gloMax

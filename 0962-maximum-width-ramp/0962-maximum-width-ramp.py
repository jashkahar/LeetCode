class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxRight = [0] * len(nums)
        i = len(nums) - 1
        prev_max = 0

        for n in reversed(nums):
            maxRight[i] = max(n, prev_max)
            prev_max = maxRight[i]
            i -= 1
        
        res = 0
        l=0

        for r in range(len(nums)):
            while nums[l] > maxRight[r]:
                l+=1
            res = max(res, r-l)
        return res

        
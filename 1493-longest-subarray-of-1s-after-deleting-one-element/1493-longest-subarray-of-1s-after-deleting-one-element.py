class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        num_zero =1
        l =0
        for r in range(len(nums)):
            num_zero -= nums[r] == 0

            if num_zero < 0:
                num_zero += nums[l] == 0
                l+=1
        return r-l
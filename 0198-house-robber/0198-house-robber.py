class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0,0
        for num in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + num)  # Update the current max
            prev2 = temp  # Update the second last value
        
        return prev1
        
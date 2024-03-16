class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen_at = {}
        
        seen_at[0] = -1
        ans ,count =0,0
        
        for i, num in enumerate(nums):
            count +=1 if num else -1
            if count in seen_at:
                ans = max(ans, i - seen_at[count])
            else:
                seen_at[count] = i
        return ans
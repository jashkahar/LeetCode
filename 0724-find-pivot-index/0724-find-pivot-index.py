class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        k = sum(nums)
        
        for r,i in enumerate(nums):
            # print(l,i,k-i)
            if(l == k-i):
                return r
            l+=i
            k -=i
            
        return -1
            
        
                
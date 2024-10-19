class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        1, 2, 3, 4
        1, 1, 2, 6
        24, 12, 4, 1

        ipt = 1, 2, 3, 4
        prefix = 24
        postfix = 24
        res = 24, 12, 8, 6 

        """
        
        prefix = 1
        postfix = 1
        res = [1]*len(nums) 

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
                        
        return(res)
            
        
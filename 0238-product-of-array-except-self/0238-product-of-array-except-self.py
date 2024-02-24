class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        res = [1]*len(nums) 
        
        #print(res)
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
            
        #print(res)
        #print("")
        
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * postfix
         #   print(res)
            postfix = postfix * nums[i]
          #  print(postfix)
           # print("")
            
        return(res)
    
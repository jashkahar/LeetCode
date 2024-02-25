class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:  
        n = len(nums)
        
        if n < 3:
            return False
        
        leftmin = [None]*n
        leftmin[0] = nums[0]
        for i in range(1,n):
            leftmin[i] =min(leftmin[i-1], nums[i])
        #print('Leftmin', leftmin)
        
        
        rightmax = [None]*n
        rightmax[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            rightmax[i] = max(rightmax[i+1], nums[i])
        #print('Rightmax', rightmax)
        
        for i in range(n):
            #print(leftmin[i], nums [i], rightmax[i])
            if(leftmin[i] < nums[i] and nums[i] < rightmax[i]):
                return True
        return False

        
#         mini = min(nums)
#         maxi = max(nums)
#         print('min:',mini)
#         print('max:',maxi)
        
#         if if(nums.index(maxi)<nums.index(mini)):
            

#         if(nums.index(maxi)>nums.index(mini)):
#             for temp in nums[mini:maxi]:
#                 print(temp)
#                 if(mini<temp<maxi):
                    
#                     return True
#                 else:
#                     return False
                
            
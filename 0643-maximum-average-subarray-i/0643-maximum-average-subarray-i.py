class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maxx= float('-inf')
        
        if len(nums) <=1:
            return nums[0]
        
        i=0
        l=k
        # print(nums[i:l])
        summ = sum(nums[i:l])
        currsum = summ
        # print(1+12-5-6)
        
        while(l < len(nums)):
            # print(currsum,currsum/k)
            currsum = currsum + nums[l] - nums [i]
            i += 1
            l += 1
            summ = max(summ, currsum)
        return summ/k
        
            
        
        
#         while(l<len(nums)):
#             print(currsum)
#             curravg = currsum/k
#             if curravg > maxx:
#                 maxx = curravg
#             print(nums[i], nums[l], currsum, curravg)
#             if(l+1<len(nums)):
#                 currsum = currsum + nums[l+1] - nums[i] 
#             i += 1
#             l += 1
            
#         return maxx
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
                
            l,r = i+1, len(nums) -1
            while l<r:
                threesum = a+nums[l] + nums[r]
                if threesum >0:
                    r -= 1
                elif threesum<0:
                    l+=1
                else:
                    res.append([a,nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                        
        return res
        
#         res = []
        
#         l1 = list(itertools.combinations(nums, 3))
#         '''
#         l2 = set(l1)
        
#         print("l1: ", l1, "\n")
#         print("l2: ", l2, "\n")'''
        
#         for i in range(len(l1)):
#             l1[i] = list(l1[i])
#         #print(l1)
        
#         for set1 in l1:
#             #print(set1, (set1[0] + set1[1] + set1[2])) 
#             if((set1[0] + set1[1] + set1[2]) == 0):
#                 #print(set1)
#                 res.append(set1)
                    
#         for i in range(len(res)):
#             res[i].sort()
#             i=i+1
        
#         temp_list = []
        
#         #print("after sort", l1)
#         for i in res:
#             if i not in temp_list:
#                 temp_list.append(i)
                
#         l1 = temp_list
#         #print(l1)
#         return l1
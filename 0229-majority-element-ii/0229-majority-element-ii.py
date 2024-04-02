class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = len(nums) // 3
        mydict = {}
        for i in range(len(nums)):
            if nums[i] in mydict.keys():
                mydict[nums[i]] +=1
            else:
                mydict.update({nums[i] : 1})
        nums = []
        for i,j in mydict.items():
            if j > m:
                nums.append(i)
        return nums
    
    #O(1) space:
#     dic = dict()
#         for i in nums:
#             if i in dic:
#                 dic[i] +=1
#             elif dic and len(dic)==2:
#                 keys = list(dic.keys())
#                 for key in keys:
#                     dic[key] -= 1
#                     if dic[key]==0:
#                         dic.pop(key)
#             else:
#                 dic[i] = 1

#         # Making sure they are repeated at least 1/3 of the population
#         for key in dic.keys():
#             dic[key] = 0
#         for i in nums:
#             if i in dic:
#                 dic[i] +=1        
#         ans = []
#         for key in dic.keys():
#             if dic[key]>len(nums)//3:
#                 ans.append(key)
        
#         return ans
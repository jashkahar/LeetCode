class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l
#         seen = set()
        
#         for i, n in enumerate(nums):
#             if nums[i] not in seen:
#                 seen.add(n)
#             elif nums[i] in seen:
#                 nums[i] = float('inf')
#                 nums.sort()
#                 # print(nums)
#             else:
#                 # print(nums)
#                 nums.sort()
#                 return i
#         return len(seen)
        
        
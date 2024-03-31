class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) space solution using boyer moore algorithm
        res, count = 0,0
        
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res


        
#         ----Hashmap Solution---
#         count = {}
        
#         res, maxCount = 0,0
        
#         for n in nums:
#             count[n] = 1 +count.get(n,0)
#             res = if count[n] > maxCount else res
#             maxCount = max(count[n], maxCount)
#         return res


#       ----Fancy hashmap colution ----
        # return list(dict(sorted(dict(Counter(nums)).items(), key = lambda x: x[1], reverse = True )))[0]
        
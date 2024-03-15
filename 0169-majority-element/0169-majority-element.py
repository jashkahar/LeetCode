class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = dict(Counter(nums))
        print(c)
        sorted_c = dict(sorted(c.items(), key = lambda x: x[1], reverse = True ))
        lc = list(sorted_c)

        print(lc)
        return lc[0]
        
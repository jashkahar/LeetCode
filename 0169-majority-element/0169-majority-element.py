class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return list(dict(sorted(dict(Counter(nums)).items(), key = lambda x: x[1], reverse = True )))[0]
        # return lc[0]
        
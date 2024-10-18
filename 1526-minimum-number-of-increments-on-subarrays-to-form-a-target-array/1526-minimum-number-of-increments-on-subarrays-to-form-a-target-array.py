class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = res =0

        for val in target:
            if val > prev:
                res+= val - prev
            prev = val
        return res
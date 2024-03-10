class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        ch = 0
        for i in gain:
            h = max(h,ch+i)
            ch += i
        return h
        
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            res = res << 1
            res = res | (n & 1)
            n = n >> 1
            # bit = (n >> 1) & 1
            # res = res | (bit << (31 - i))
        return res
            
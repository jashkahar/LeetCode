class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        i = 5
        while n >= i:
            res += n // i
            i *= 5  # Increment i by multiplying by 5 each time to get powers of 5
        return res
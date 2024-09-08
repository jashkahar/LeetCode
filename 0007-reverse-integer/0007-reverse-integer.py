class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31 //10 #-2147483648
        MAX = 2**31-1 //10 #2147483647


        res = 0

        while x!=0:
            digit = int(math.fmod(x, 10))
            x = int(x/10)

            if (res > MAX or 
               (res == MAX and digit >= 7)):
                return 0
            if (res < MIN or 
               (res == MIN and digit <= 8)):
                return 0
            res = (res * 10) + digit
        return res
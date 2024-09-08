class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31 #-2147483648
        MAX = 2**31-1 #2147483647
        print(MAX // 10)
        print(MAX%10)

        res = 0

        while x!=0:
            digit = int(math.fmod(x, 10))
            x = int(x/10)

            if (res > 214748364 or 
               (res == 214748364 and digit >= 7 )):
                return 0
            if (res < MIN // 10 or 
               (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit
        return res
class Solution:
    def sumofsq(self, n: int) -> int:
        output = 0
        
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
        
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.sumofsq(n)
            
            if n == 1:
                return True
            
        return False
    
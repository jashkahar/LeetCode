class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n < 2:
            return n
        
        i = j = 0
        
        while i < n:
            c = 1
            print(chars[i])
            while i < n-1 and chars[i] == chars[i+1]:
                c += 1
                i += 1
            
            chars[j] = chars[i]
            j += 1
            if c > 1:
                for val in str(c):
                    chars[j] = val
                    j += 1
            i += 1
        
        return j
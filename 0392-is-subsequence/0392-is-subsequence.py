class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        lt = list(t)
        ls = list(s)
        
        n = len(ls)
        m = len(lt)
        
        i , j = 0, 0
        
        if n == 0:
            return True
        if m == 0:
            return False
        
        while j< m:
            # print("searching", ls[i])
            # print("current j:", lt[j])
            if ls[i] == lt[j]:
                # print("Found")
                i += 1
                j += 1
                if i == n:
                    return True
            else:
                j += 1
        return False
        
        
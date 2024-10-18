class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        val =set()
        
        for c in dict(Counter(arr)).values():
            if c not in val:
                val.add(c)
            else:
                return False
            
        return True
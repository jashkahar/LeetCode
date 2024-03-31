class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1
                    
        
#         if(len(haystack) == 1):
#             if haystack == needle:
#                 return 0
#             else:
#                 return -1

#         elif(haystack.find(needle)>=0):
#             return(haystack.find(needle))
#         else:
#             return -1
            
        
        
        
        
        
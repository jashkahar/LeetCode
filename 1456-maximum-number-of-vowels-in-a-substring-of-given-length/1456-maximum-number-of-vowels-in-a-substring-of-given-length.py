class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vovels = {'a','e','i','o','u'}
        
        s = list(s)
        
        l=0
        r=k
        
        maxvovels = 0
        
        for i in s[l:r]:
            if i in vovels:
                maxvovels += 1
        
        currvovels = maxvovels
        
        while(r<len(s)):
            if(s[l] in vovels):
                currvovels -= 1
            if(s[r] in vovels):
                currvovels += 1
            l += 1
            r += 1
            maxvovels = max(maxvovels, currvovels)
        return maxvovels
    
    
#     for i in s[l:r]:
#                 if i in vovels:
#                     currvovels +=1
#                 # print(s[l:r], currvovels)
#             # print(" ")
#             maxvovels = max(maxvovels, currvovels)
#             l += 1
#             r += 1
        
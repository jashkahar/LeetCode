class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        tmp = [0 for a in range(N+1)]
        
        for i,v in enumerate(citations):
            if v>N:
                tmp[N] += 1
            else:
                tmp[v] += 1
        total = 0
        for i in range(N, -1, -1):
            total += tmp[i]
            if total >= i:
                return i
#         Slower
#         N= len(citations)
        
#         citations.sort()
        
#         for i,v in enumerate(citations):
#             if N-i <= v:
#                 return N-i
#         return 0
        
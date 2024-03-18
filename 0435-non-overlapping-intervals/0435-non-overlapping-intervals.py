class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        
        currmin = intervals[0][1]
        res = 0
        
        for start, end in intervals[1:]:
            if start >= currmin:
                currmin = end
            else:
                res+=1
                currmin = min(currmin, end)
        return res
        
                    
            
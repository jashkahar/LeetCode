class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        resultSum = sum(nums[:2])
        minDiff = float('inf')
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            
            while left<right:
                curSum = nums[i] + nums [left] + nums[right]
                
                if curSum == target:
                    return target
                if curSum < target:
                    left += 1
                else:
                    right -= 1
                
                diffToTarget = abs(curSum - target)
                
                if diffToTarget < minDiff:
                    resultSum = curSum
                    minDiff = diffToTarget
                    
        return resultSum
            
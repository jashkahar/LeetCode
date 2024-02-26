class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        maxx = 0
        while(left<right):
            currmax = (min(height[left],height[right]) * abs(right - left))
            
            if(maxx<currmax):
                maxx = currmax
            if(height[left]<height[right]):
                left += 1
            else:
                right -= 1
                
            
        return maxx
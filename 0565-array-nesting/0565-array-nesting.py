class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)  # To mark elements as visited
        max_length = 0
        
        for i in range(len(nums)):
            if not visited[i]:
                length = 0
                current = i
                # Follow the sequence until a cycle is detected
                while not visited[current]:
                    visited[current] = True
                    current = nums[current]
                    length += 1
                max_length = max(max_length, length)
        
        return max_length

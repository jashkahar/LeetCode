class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]
        # goal = len(nums)-1

        # for i in range(len(nums)-1, -1, -1):
        #     # print(i, nums[i], goal)
        #     if i + nums[i] >= goal:
        #         goal = i

        # return True if goal == 0 else False

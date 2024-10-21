class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-1], 0

        for i in range(len(cost) - 2, -1, -1):
            tmp = one
            one = min(one, two) + cost[i]
            two = tmp

        return min(one, two)
        # cost.append(0)
        
        # for i in range(len(cost)-3, -1, -1):
        #     cost[i] += min(cost[i+1], cost[i+2])
        # return min(cost[0], cost[1])
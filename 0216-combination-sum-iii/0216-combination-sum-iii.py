class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(combination, n, start):
            if k == len(combination):
                if n == 0:
                    result.append(combination.copy())
                    return
            for i in range(start, 10):
                combination.append(i)
                backtrack(combination, n-i, i+1)
                combination.pop()
        backtrack([],n,1)
        return result
        
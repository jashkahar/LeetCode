class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maximum=max(candies)
        greatest=[]
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                greatest.append(True)
            else:
                greatest.append(False)

        return greatest
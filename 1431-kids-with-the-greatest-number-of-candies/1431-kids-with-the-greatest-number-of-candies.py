class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maximum=max(candies)
        #print(maximum)
        greatest=[]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                #print(candies[i],'true')
                greatest.append(True)
            else:
                #print(candies[i],'false')
                greatest.append(False)
        #print(greatest) 
        return greatest
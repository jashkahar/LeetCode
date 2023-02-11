class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mySet = set(nums)
        maxvalue = 0
        maxelement = 0
        countOfChars = defaultdict(int)
        for element in mySet:
            countOfChar = nums.count(element)
            countOfChars[element] = countOfChar
            if countOfChars[element] > n/2 and countOfChars[element] > maxvalue:
                maxvalue=countOfChars[element]
                maxelement = element

        return maxelement
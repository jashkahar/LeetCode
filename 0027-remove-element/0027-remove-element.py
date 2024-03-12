class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        
        # print(nums)
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                # print(nums)
                k+=1
        return k
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set, nums2set = set(nums1), set(nums2)
        answer = [[],[]]
        for i in nums1set:
            if i not in nums2set:
                answer[0].append(i)
        for i in nums2set:
            if i not in nums1set:
                answer[1].append(i)
                
        return answer
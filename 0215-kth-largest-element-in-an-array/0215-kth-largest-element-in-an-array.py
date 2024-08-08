class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k+1
        heapq.heapify(nums)

        while k:
            res = heapq.heappop(nums)
            k -=1
        return res

        # # exmaple 3
        # min_heap = []
        # for num in nums:
        #     heapq.heappush(min_heap, num)

        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        
        # return min_heap[0]
# example 2
#         k = len(nums) - k
        
#         def quickselect(l,r):
#             pivot, p = nums[r], l
#             for i in range(l,r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p += 1
#             nums[p], nums[r] = nums[r], nums[p]
            
#             if p>k: return quickselect(l, p-1)
#             elif p<k: return quickselect(p+1, r)
#             else: return nums[p]
        
#         return quickselect(0, len(nums)-1)

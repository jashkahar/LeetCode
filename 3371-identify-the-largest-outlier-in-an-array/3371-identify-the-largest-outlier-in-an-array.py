class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        max_outlier = min(nums)

        for num in nums:
            required_sum = total_sum - num
            if required_sum % 2 != 0:
                continue
            potential_sum = required_sum // 2
            freq_map[num] -= 1

            if freq_map[num] == 0:
                del freq_map[num]

            if potential_sum in freq_map and freq_map[potential_sum] > 0:
                max_outlier = max(max_outlier, num)

            freq_map[num] = freq_map.get(num,0)+1
        return max_outlier
        
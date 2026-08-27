class Solution(object):
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0

        nums = sorted(nums)

        max_gap = 0

        for i in range(1, n):
            gap = nums[i] - nums[i - 1]
            max_gap = max(max_gap, gap)

        return max_gap
        
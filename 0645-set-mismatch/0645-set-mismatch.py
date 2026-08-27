class Solution(object):
    def findErrorNums(self, nums):

        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        n = len(nums)
        total = n * (n + 1) // 2
        actual_sum = sum(nums)

        missing = total - (actual_sum - duplicate)

        return [duplicate, missing]
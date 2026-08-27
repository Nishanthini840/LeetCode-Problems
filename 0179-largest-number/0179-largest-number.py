class Solution(object):
    def largestNumber(self, nums):

        nums = [str(x) for x in nums]

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):

                a = nums[i]
                b = nums[j]

                if a + b < b + a:
                    nums[i], nums[j] = nums[j], nums[i]

        result = ""

        for num in nums:
            result += num

        if result[0] == "0":
            return "0"

        return result
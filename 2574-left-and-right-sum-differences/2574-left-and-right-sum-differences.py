class Solution:
    def leftRightDifference(self, nums):
        answer = []
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            right = right - nums[i]
            answer.append(abs(left - right))
            left = left + nums[i]

        return answer 
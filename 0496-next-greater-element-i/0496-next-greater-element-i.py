class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}

        for num in nums2:

            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num

            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        result = []

        for num in nums1:
            result.append(next_greater[num])

        return result
        
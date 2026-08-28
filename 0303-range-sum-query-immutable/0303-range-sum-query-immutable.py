class NumArray(object):

    def __init__(self, nums):
        self.prefix = [0]

        current_sum = 0

        for num in nums:
            current_sum += num
            self.prefix.append(current_sum)


    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
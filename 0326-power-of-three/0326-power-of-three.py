class Solution:
    def isPowerOfThree(self, n):

        while n > 0 and n % 3 == 0:
            n = n // 3

        return n == 1
        
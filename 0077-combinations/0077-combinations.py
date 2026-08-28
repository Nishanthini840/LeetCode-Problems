class Solution(object):
    def combine(self, n, k):

        result = []

        def backtrack(start, current):

            if len(current) == k:
                result.append(current[:])
                return

            for num in range(start, n + 1):
                current.append(num)
                backtrack(num + 1, current)
                current.pop()

        backtrack(1, [])

        return result
        
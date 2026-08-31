class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []

        i = 0

        while i < len(temperatures):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                previous = stack.pop()

                answer[previous] = i - previous

            stack.append(i)

            i += 1

        return answer
        
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = list(s)

        for i in range(len(s)):

            if s[i] == "(":
                stack.append(i)

            elif s[i] == ")":

                if stack:
                    stack.pop()
                else:
                    result[i] = ""

        while stack:
            index = stack.pop()
            result[index] = ""

        return "".join(result)
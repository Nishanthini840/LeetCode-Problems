class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen = set()
        result = set()

        for i in range(len(s) - 9):
            part = s[i:i + 10]

            if part in seen:
                result.add(part)
            else:
                seen.add(part)

        return list(result)
        
class Solution:
    def isAcronym(self, words, s):
        result = ""
        for i in words:
            result = result+i[0]
        return result == s

        
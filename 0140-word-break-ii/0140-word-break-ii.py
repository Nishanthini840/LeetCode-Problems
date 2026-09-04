class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = []

        def backtrack(start, path):

            if start == len(s):
                result.append(" ".join(path))
                return

            for word in wordDict:

                if s[start:start + len(word)] == word:
                    path.append(word)

                    backtrack(start + len(word), path)

                    path.pop()

        backtrack(0, [])

        return result
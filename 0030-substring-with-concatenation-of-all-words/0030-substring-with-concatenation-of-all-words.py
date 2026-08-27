class Solution:
    def findSubstring(self, s, words):
        res = []
        w = len(words[0])
        total = w * len(words)
        count = Counter(words)

        for i in range(len(s) - total + 1):
            seen = Counter(s[j:j+w] for j in range(i, i+total, w))
            if seen == count:
                res.append(i)

        return res 
        
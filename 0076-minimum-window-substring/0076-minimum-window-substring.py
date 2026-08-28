class Solution(object):
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        count = 0
        min_len = float("inf")
        start = 0

        for right in range(len(s)):

            char = s[right]

            if char in need:
                need[char] -= 1

                if need[char] >= 0:
                    count += 1

            while count == len(t):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]

                if left_char in need:
                    need[left_char] += 1

                    if need[left_char] > 0:
                        count -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]
        
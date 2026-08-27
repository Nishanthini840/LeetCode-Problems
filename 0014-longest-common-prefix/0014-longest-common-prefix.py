class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ref = strs[0]
        for char_index in range(len(ref)):
            curr_char = ref[char_index]
            for word in strs[1:]:
                if char_index == len(word) or word[char_index] != curr_char:
                    return ref[:char_index]
        return ref
        
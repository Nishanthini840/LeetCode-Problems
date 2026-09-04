class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        heap = []

        for ch in count:
            heapq.heappush(heap, (-count[ch], ch))

        result = ""
        prev_count = 0
        prev_char = ""

        while heap:

            count, ch = heapq.heappop(heap)

            result += ch

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            count += 1

            prev_count = count
            prev_char = ch

        if len(result) != len(s):
            return ""

        return result
        
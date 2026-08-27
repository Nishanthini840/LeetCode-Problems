class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        heap = []
        for char,freq in count.items():
            heapq.heappush(heap,(-freq,char))
        res = ""
        while heap:
            freq,char = heapq.heappop(heap)
            res += char*(-freq)
        return res

        
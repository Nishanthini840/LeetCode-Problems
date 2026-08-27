class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x,y in points:
            distance = x * x + y * y
            heapq.heappush(heap,(-distance ,x,y))

            if len(heap) > k:
                heapq.heappop(heap)
        return [[x,y] for distance,x,y in heap]



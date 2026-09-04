class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = float('inf')

        dist = [INF] * n

        dist[src] = 0

        for _ in range(k + 1):

            new_dist = dist[:]

            for from_city, to_city, price in flights:

                if dist[from_city] != INF:

                    new_dist[to_city] = min(new_dist[to_city], dist[from_city] + price)

            dist = new_dist

        if dist[dst] == INF:
            return -1

        return dist[dst]
        
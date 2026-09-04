class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        visited = [False] * n
        distance = [float('inf')] * n

        distance[0] = 0
        total = 0

        for _ in range(n):

            cur = -1

            for i in range(n):
                if not visited[i]:
                    if cur == -1 or distance[i] < distance[cur]:
                        cur = i

            visited[cur] = True
            total += distance[cur]

            for i in range(n):
                if not visited[i]:

                    x = abs(points[cur][0] - points[i][0])
                    y = abs(points[cur][1] - points[i][1])

                    cost = x + y

                    if cost < distance[i]:
                        distance[i] = cost

        return total
        
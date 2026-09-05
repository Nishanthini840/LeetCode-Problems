import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = {}

        for u, v, time in times:
            if u not in graph:
                graph[u] = []

            graph[u].append((v, time))

        heap = [(0, k)]
        visited = set()
        max_time = 0

        while heap:

            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = max(max_time, time)

            for neighbor, travel_time in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(
                        heap,
                        (time + travel_time, neighbor)
                    )

        if len(visited) == n:
            return max_time

        return -1
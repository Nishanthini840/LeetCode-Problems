import heapq

class Solution(object):
    def minimumEffortPath(self, heights):

        rows = len(heights)
        cols = len(heights[0])

        heap = [(0, 0, 0)]
        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while heap:

            effort, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return effort

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    new_effort = max(
                        effort,
                        abs(heights[r][c] - heights[nr][nc])
                    )

                    heapq.heappush(
                        heap,
                        (new_effort, nr, nc)
                    )
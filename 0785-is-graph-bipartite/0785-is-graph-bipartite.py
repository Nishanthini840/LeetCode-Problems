class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = [-1] * len(graph)

        for i in range(len(graph)):
            if color[i] != -1:
                continue

            color[i] = 0
            queue = [i]

            while queue:
                node = queue.pop(0)

                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False

        return True
        
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        safe = {}

        def dfs(node):

            if node in safe:
                return safe[node]

            safe[node] = False

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            safe[node] = True
            return True

        result = []

        for node in range(len(graph)):
            if dfs(node):
                result.append(node)

        return result
        
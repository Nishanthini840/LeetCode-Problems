import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = [[] for _ in range(n)]

        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))

        probability = [0.0] * n
        probability[start_node] = 1.0

        heap = [(-1.0, start_node)]

        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob

            if node == end_node:
                return prob

            if prob < probability[node]:
                continue

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob

                if new_prob > probability[neighbor]:
                    probability[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0
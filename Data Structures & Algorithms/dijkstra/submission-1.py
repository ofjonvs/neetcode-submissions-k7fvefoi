class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        sp = {node: -1 for node in range(n)}
        adj = [[] for _ in range(n)]
        for v1, v2, w in edges:
            adj[v1].append((v2, w))

        queue = [(0, src)]
        while queue:
            weight, node = heapq.heappop(queue)
            if sp[node] != -1:
                continue
            sp[node] = weight
            for neighbor, neighWeight in adj[node]:
                heapq.heappush(queue, (neighWeight+weight, neighbor))
        return sp

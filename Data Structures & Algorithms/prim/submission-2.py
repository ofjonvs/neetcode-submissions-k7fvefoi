class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for start, end, weight in edges:
            adj[start].append((end, weight))
            adj[end].append((start, weight))
        heap = [(0, 0)]
        processed = set()
        totWeight = 0
        while heap and len(processed) != n:
            weight, v = heapq.heappop(heap)
            if v in processed:
                continue
            processed.add(v)
            totWeight += weight
            for neighbor, nWeight in adj[v]:
                neighbor not in processed and heapq.heappush(heap, (nWeight, neighbor))
        return totWeight if len(processed) == n else -1
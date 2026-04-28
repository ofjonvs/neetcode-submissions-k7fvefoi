class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        dist, adj = [float('inf')]*(n+1), [[] for _ in range(n+1)]
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))

        while heap:
            w, v = heapq.heappop(heap)
            if w < dist[v]:
                dist[v] = w
                for neigh, weigh in adj[v]:
                    heapq.heappush(heap, (weigh+dist[v], neigh))
            
        res = max(dist[1:])
        return -1 if res == float('inf') else res
            


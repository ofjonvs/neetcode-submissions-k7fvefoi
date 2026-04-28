class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        dist, adj = [None]*(n+1), [[] for _ in range(n+1)]
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))

        while n and heap:
            w, v = heapq.heappop(heap)
            if dist[v] is None:
                dist[v] = w
                n -= 1
                for neigh, weigh in adj[v]:
                    heapq.heappush(heap, (weigh+dist[v], neigh))
            
        return -1 if n else dist[v]
            


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:   
        adj = {}
        for s, d, w in flights:
            adj.setdefault(s, []).append((d, w))
        heap = [(0, src, 0)]
        
        while heap:
            w, d, stops = heapq.heappop(heap)
            if d == dst:
                return w
            if stops <= k:
                for nb, nw in adj.get(d, []):
                    heapq.heappush(heap, (w+nw, nb, stops+1))
        return -1
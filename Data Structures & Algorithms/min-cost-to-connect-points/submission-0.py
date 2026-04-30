class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = [[] for _ in range(len(points))]
        for i, (xi, yi) in enumerate(points):
            for j, (xj, yj) in enumerate(points):
                if i == j:
                    continue
                adj[i].append((j, abs(xi-xj) + abs(yi-yj)))
        
        heap = [(0, 0)]
        processed = set()
        totDist = 0
        while len(processed) < len(points) and heap:
            dist, point = heapq.heappop(heap)
            if point in processed or processed.add(point):
                continue
            totDist += dist
            for neighbor, nDist in adj[point]:
                neighbor in processed or heapq.heappush(heap, (nDist, neighbor))
        return totDist
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [[None, 0] for _ in range(len(points))]
        def find(point):
            while parents[point][0] is not None:
                point = parents[point][0]
            return point

        def union(point1, point2):
            parent1, parent2 = find(point1), find(point2)
            if parent1 == parent2:
                return True
            parents[parent1][0] = parent2
            return False
        
        heap = []
        for point1, (x1, y1) in enumerate(points):
            for point2, (x2, y2) in enumerate(points):
                if point1 == point2:
                    continue
                heapq.heappush(heap, (abs(x1-x2)+abs(y1-y2), point1, point2))
        
        seenPoints = set()
        totDist = 0
        numEdges = 0
        while numEdges != len(points)-1:
            dist, point1, point2 = heapq.heappop(heap)
            if union(point1, point2):
                continue
            seenPoints.add(point1), seenPoints.add(point2)
            totDist += dist
            numEdges += 1
        return totDist
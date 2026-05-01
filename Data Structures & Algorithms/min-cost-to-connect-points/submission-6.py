class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [[None, 1] for _ in range(len(points))]
        def find(point):
            if parents[point][0] is not None:
                point = find(parents[point][0])
            return point

        def union(point1, point2):
            parent1, parent2 = find(point1), find(point2)
            if parent1 == parent2:
                return True
            big, small = (parent1, parent2) if parents[parent1][1] > parents[parent2][1] else (parent2, parent1)
            parents[small][0] = big
            parents[big][1] += parents[small][1]
            return False
        
        heap = []
        for point1, (x1, y1) in enumerate(points):
            for point2, (x2, y2) in enumerate(points[point1+1:], start=point1+1):           
                heapq.heappush(heap, (abs(x1-x2)+abs(y1-y2), point1, point2))
        
        totDist = 0
        numEdges = 0
        while numEdges != len(points)-1:
            dist, point1, point2 = heapq.heappop(heap)
            if union(point1, point2):
                continue
            totDist += dist
            numEdges += 1
        return totDist
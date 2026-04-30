class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        heap = [(1, start_node)]
        adjList = [[] for _ in range(n)]
        for (start, end), prob in zip(edges, succProb):
            adjList[start].append((end, prob))
            adjList[end].append((start, prob))
        processed = set()
        while heap:
            prob, v = heapq.heappop_max(heap)
            processed.add(v)
            if v == end_node:
                return prob
            for neighbor, nProb in adjList[v]:
                neighbor not in processed and heapq.heappush_max(heap, (prob*nProb, neighbor))
        return 0
            
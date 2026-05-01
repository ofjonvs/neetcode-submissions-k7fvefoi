class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for i, (v1, v2, w) in enumerate(edges):
            adj[v1].append((v2, w, i))
            adj[v2].append((v1, w, i))

        def buildMst(excludeEdge=None, inclEdge=None):
            processed = set()
            if inclEdge is None:
                heap = [(0, 0)]
                totWeight = 0
            else:
                v1, v2, w = edges[inclEdge]
                totWeight = w
                heap = [(0, v1), (0, v2)]
            while heap and n != len(processed):
                w, v = heapq.heappop(heap)
                if v in processed:
                    continue
                processed.add(v)
                totWeight += w
                for nv, nw, ne in adj[v]:
                    if excludeEdge == ne:
                        continue
                    heapq.heappush(heap, (nw, nv))
            return totWeight if len(processed) == n else -1
        
        fullMst = buildMst()
        crit, pseud = [], []
        for i in range(len(edges)):
            if (mst:=buildMst(i)) != fullMst:
                crit.append(i)
            elif fullMst == buildMst(inclEdge=i):
                pseud.append(i)

        return [crit, pseud]



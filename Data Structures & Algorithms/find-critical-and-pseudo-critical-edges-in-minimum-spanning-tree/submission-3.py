class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])

        def buildMst(exEdge=None, incEdge=None):
            parents = [[None, 1] for _ in range(n)]
            def find(v):
                if parents[v][0] is not None:
                    parents[v][0] = find(parents[v][0])
                    return parents[v][0]
                return v

            def union(v1, v2):
                parent1, parent2 = find(v1), find(v2)
                if parent1 == parent2:
                    return True
                big, small = (parent1, parent2) if parents[parent1][1] > parents[parent2][1] else (parent2, parent1)
                parents[small][0] = big
                parents[big][1] += parents[small][1]
                return False
            
            if incEdge is None:
                numEdges = totWeight = 0
            else:
                numEdges = 1
                totWeight = incEdge[1]
                exEdge = incEdge[0]
                union(incEdge[2], incEdge[3])
            for v1, v2, w, i in edges:
                if i == exEdge or union(v1, v2):
                    continue
                totWeight += w
                numEdges += 1
                if numEdges == n-1:
                    return totWeight
            return -1
        
        fullMst = buildMst()
        crit, pseud = [], []
        for v1, v2, w, i in edges:
            if buildMst(i) != fullMst:
                crit.append(i)
            else:
                if buildMst(incEdge=(i, w, v1, v2)) == fullMst:
                    pseud.append(i)
        return [crit, pseud]



        

            

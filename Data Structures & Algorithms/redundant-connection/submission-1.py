class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.nodes = [[None, 1] for _ in range(len(edges)+2)] # (parent, size)
        def getParent(v):
            if self.nodes[v][0] is None:
                return v
            self.nodes[v][0] = getParent(self.nodes[v][0])
            return self.nodes[v][0]
        
        def union(v1, v2):
            pv1, pv2 = getParent(v1), getParent(v2)
            if pv1 == pv2:
                return True

            big, small = (pv1, pv2) if self.nodes[pv1][1] > self.nodes[pv2][1] else (pv2, pv1)
            self.nodes[small][0] = big
            self.nodes[big][1] += self.nodes[small][1]
            return False

        return next(edge for edge in edges if union(*edge))

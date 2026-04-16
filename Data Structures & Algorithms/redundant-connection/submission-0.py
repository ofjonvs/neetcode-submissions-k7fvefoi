class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.nodes = [None]*(len(edges)+1) # (parent, size)
        def getParent(v):
            while self.nodes[v] is not None:
                v = self.nodes[v]
            return v
        
        def union(v1, v2):
            if getParent(v1) == getParent(v2):
                return True
            self.nodes[getParent(v1)] = getParent(v2)
            return False
        
        return next(edge for edge in edges if union(*edge))

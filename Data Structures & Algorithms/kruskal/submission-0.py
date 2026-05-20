class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        class ufNode:
            def __init__(self, parent, size):
                self.parent, self.size = parent, size

        uf = [ufNode(None, 1) for _ in range(n)]
        def find(node):
            if uf[node].parent is None:
                return node
            uf[node].parent = find(uf[node].parent)
            return uf[node].parent

        def union(node1, node2):
            if (parent1:=find(node1)) == (parent2:=find(node2)):
                return True
            big, small = (parent1, parent2) if parent1 > parent2 else (parent2, parent1)
            uf[small].parent = big
            uf[big].size += uf[small].size
            return False
        
        edges.sort(key=lambda x: x[2])
        totWeight = numEdges = 0
        for v1, v2, weight in edges:
            if union(v1, v2):
                continue
            numEdges += 1
            totWeight += weight
            if numEdges == n - 1:
                return totWeight

        return -1

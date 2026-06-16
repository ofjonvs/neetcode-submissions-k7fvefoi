class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class Node:
            def __init__(self, parent, size):
                self.parent = parent
                self.size = size

        uf = [Node(None, 0) for _ in range(n)]
        numSets = n
        def getParent(node):
            path = []
            while uf[node].parent is not None:
                path.append(node)
                node = uf[node].parent
            for n in path:
                uf[n].parent = node
            return node

        def isUnion(node1, node2):
            parent1, parent2 = getParent(node1), getParent(node2)
            if parent1 == parent2:
                return True
            union(parent1, parent2)
            nonlocal numSets 
            numSets -= 1
            return False
        
        def union(node1, node2):
            big, small = (node1, node2) if uf[node1].size > uf[node2].size else (node2, node1)
            uf[small].parent = big

        for node1, node2 in edges:
            if isUnion(node1, node2):
                return False

        return numSets == 1

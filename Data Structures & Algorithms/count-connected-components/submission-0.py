class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class Node:
            def __init__(self):
                self.parent = None
                self.rank = 0

        nodes = [Node() for _ in range(n)]
        numComponents = n
        def find(node):
            if nodes[node].parent is None:
                return node
            nodes[node].parent = find(nodes[node].parent)
            return nodes[node].parent

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 != root2:
                big, small = (root1, root2) if nodes[root1].rank > nodes[root2].rank else (root2, root1)
                nodes[small].parent = big
                return 1
            return 0
            

        for v1, v2 in edges:
            numComponents -= union(v1, v2)
        
        return numComponents
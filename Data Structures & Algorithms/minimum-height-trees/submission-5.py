class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        adj = [set() for _ in range(n)]
        degs = [0]*n
        for v1, v2 in edges:
            adj[v1].add(v2), adj[v2].add(v1)
            degs[v1] += 1
            degs[v2] += 1
        leaves = {v for v, d in enumerate(degs) if d == 1}
        leaves = deque(leaves)
        while n > 2:
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                for nv in adj[leaf]:
                    n -= 1
                    if nv not in leaves:
                        adj[nv].remove(leaf)
                        degs[nv] -= 1
                        if degs[nv] == 1:
                            leaves.append(nv)
                        
        return list(leaves)
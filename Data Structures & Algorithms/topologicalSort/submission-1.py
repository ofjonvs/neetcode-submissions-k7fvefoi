class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v2].append(v1)

        order = []
        seen = set()
        for i in range(n):
            curPath = set()
            def dfs(v):
                isCycle = False
                if v in curPath:
                    return True
                if v in seen:
                    return False
                curPath.add(v), seen.add(v)
                for neighbor in adj[v]:
                    isCycle = dfs(neighbor) or isCycle
                order.append(v)
                curPath.remove(v)
                return isCycle
    
            isCycle = dfs(i)
            if isCycle:
                return []
            if len(seen) == n:
                break
        return order
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].add(v2), adj[v2].add(v1)
        heights = [None]*n
        minHeight = n
        for root in range(n):
            height = 0
            queue = deque([root])
            dontAdd = set()
            cachedMinHeight = n
            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()
                    dontAdd.add(node)
                    if heights[node] is not None:
                        cachedMinHeight = min(heights[node], cachedMinHeight)
                    for child in adj[node]:
                        if child not in dontAdd:
                            queue.append(child)
                height += 1
            minHeight = min(minHeight, height, cachedMinHeight)
            heights[root] = height
        return [root for root in range(n) if heights[root] == minHeight]
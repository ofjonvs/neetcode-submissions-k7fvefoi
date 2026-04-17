class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        class Vertex:
            def __init__(self):
                self.parent = None
                self.size = 1
        graph = {}
        def union(v1, v2):
            def find(v):
                if graph[v].parent is None:
                    return v
                graph[v].parent = find(graph[v].parent)
                return graph[v].parent
            root1, root2 = find(v1), find(v2)
            if root1 == root2:
                return 0
            big, small = (root1, root2) if graph[root1].size > graph[root2].size else (root2, root1)
            graph[small].parent = big
            graph[big].size += graph[small].size
            return graph[big].size

        longSeq = 1
        for num in nums:
            if num in graph:
                continue
            graph[num] = Vertex()
            for neighbor in (num-1, num+1):
                if neighbor in graph:
                    longSeq = max(union(num, neighbor), longSeq)
        return longSeq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        tickets.sort(reverse=True)
        for src, dst in tickets:
            graph.setdefault(src, []).append(dst)
        out = []
        def dfs(src):
            while graph.get(src):
                dfs(graph[src].pop())
            out.append(src)
        dfs('JFK')
        return out[::-1]
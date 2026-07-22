class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        tickets.sort()
        for src, dst in tickets:
            graph.setdefault(src, []).append(dst)
        out = ['JFK']
        def dfs(src):
            if len(out) == len(tickets) + 1:
                return True
            if src not in graph:
                return False
            
            for i in range(len(graph[src])):
                dst = graph[src].pop(i)
                out.append(dst)
                if dfs(dst):
                    return True
                graph[src].insert(i, dst)
                out.pop()
            return False
        dfs('JFK')
        return out
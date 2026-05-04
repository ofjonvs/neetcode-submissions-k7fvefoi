class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            adj[c1].append(c2)
        
        order = []
        visit = set()
        prereqs = [set() for _ in range(numCourses)]
        for course in range(numCourses):
            def search(i):
                if i in visit:
                    return prereqs[i].union({i})
                visit.add(i)
                for course in adj[i]:
                    prereqs[i].update(search(course))
                return prereqs[i].union({i})
            search(course)
        return [c2 in prereqs[c1] for c1, c2 in queries]

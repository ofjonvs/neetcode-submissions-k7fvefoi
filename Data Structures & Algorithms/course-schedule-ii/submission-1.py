class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for course1, course2 in prerequisites:
            adj[course1].append(course2)

        order = []
        seen = set()
        for i in range(numCourses):
            inPath = set()
            def dfs(course):
                isValid = True
                if course in inPath:
                    return False
                if course in seen:
                    return True
                seen.add(course), inPath.add(course)
                for prereq in adj[course]:
                    isValid = dfs(prereq) and isValid
                order.append(course)
                inPath.remove(course)
                return isValid

            if not dfs(i):
                return []
            if len(seen) == numCourses:
                break
        return order
                
                
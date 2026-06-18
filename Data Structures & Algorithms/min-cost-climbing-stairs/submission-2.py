class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def cache(func):
            funcCache = [None]*len(cost)*2
            def recurse(i):
                if funcCache[i] is None:
                    funcCache[i] = func(i)
                return funcCache[i]
            return recurse
            
        @cache
        def recurse(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(recurse(i+1), recurse(i+2))
        return min(recurse(0), recurse(1))
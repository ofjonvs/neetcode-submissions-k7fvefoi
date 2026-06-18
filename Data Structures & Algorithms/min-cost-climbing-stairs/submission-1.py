class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import cache

        @cache
        def recurse(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(recurse(i+1), recurse(i+2))
        return min(recurse(0), recurse(1))
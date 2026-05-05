class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        from functools import lru_cache

        @lru_cache(capacity*len(profit))
        def helper(i, curCap):
            if i == len(profit):
                return 0
            newCap = curCap-weight[i]
            newProf = None
            return max(profit[i]+helper(i+1, newCap) if newCap >= 0 else 0, helper(i+1, curCap))
        return helper(0, capacity)
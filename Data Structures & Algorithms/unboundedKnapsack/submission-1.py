class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        from functools import lru_cache

        @lru_cache(len(profit)*capacity)
        def recurse(i, cap):
            if i >= len(profit):
                return 0
            if weight[i] + cap > capacity:
                return recurse(i+1, cap)
            return max(profit[i] + recurse(i, cap+weight[i]), recurse(i+1, cap))
        
        return recurse(0, 0)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache

        @cache
        def rec(i, hold):
            if i >= len(prices):
                return 0
            return max(rec(i+1, hold), rec(i+1, not hold) + prices[i]*(hold and 1 or -1))
        
        return rec(0, False)
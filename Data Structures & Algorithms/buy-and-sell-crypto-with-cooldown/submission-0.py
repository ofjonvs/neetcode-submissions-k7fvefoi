class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache

        @cache
        def recurse(day, hold):
            if day == len(prices)-1:
                return prices[day] if hold else 0
            if day >= len(prices):
                return 0
            
            if hold:
                return max(prices[day] + recurse(day+2, False), recurse(day+1, True))
            else:
                return max(recurse(day+1, True) - prices[day], recurse(day+1, False))
        
        return recurse(0, False)
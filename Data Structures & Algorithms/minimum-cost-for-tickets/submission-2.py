class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(365*3)
        def helper(idx, passDays):
            return 0 if idx >= len(days) else \
            helper(idx+1, passDays) if passDays > days[idx] else \
            min(cost + helper(idx+1, numPassDays+days[idx]) for cost, numPassDays in zip(costs, (1, 7, 30)))

        return helper(0, 0)
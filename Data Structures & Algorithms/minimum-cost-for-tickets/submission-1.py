class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(365*3)
        def helper(idx, passDays):
            return 0 if idx >= len(days) else \
            helper(idx+1, passDays) if passDays > days[idx] else \
            min(costs[0] + helper(idx+1, 0), costs[1] + helper(idx+1, 7+days[idx]), costs[2] + helper(idx+1, 30+days[idx]))

        return helper(0, 0)
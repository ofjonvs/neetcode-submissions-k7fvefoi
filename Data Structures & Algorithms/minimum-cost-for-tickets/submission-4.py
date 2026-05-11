class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = [0]*31
        lastDay = cumCost = 0
        for day in days:
            cache = cache[day-lastDay:] + [cache[-1]]*(day-lastDay-1)
            cache.append(min(costs[0]+cache[-1], costs[1]+cache[-7], costs[2]+cache[-30]))
            lastDay=day
        return cache[-1]
                
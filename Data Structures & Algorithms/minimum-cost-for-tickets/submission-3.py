class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = [0]*31
        lastDay = cumCost = 0
        for day in days:
            cache = cache[day-lastDay:] + [cache[-1]]*(day-lastDay)
            # print(cache, 1)
            # print(costs[0]+cache[-1], costs[1]+cache[-7], costs[2]+cache[-30])
            cache[-1] = min(costs[0]+cache[-2], costs[1]+cache[-8], costs[2]+cache[-31])
            # for d in range(31-day-lastDay, 31):
            #     cache[d] = min(costs[0]+cache[d-1], costs[1]+cache[d-7], costs[2]+cache[d-30])
            # for i, daysBack in enumerate((1, 7, 30)):
            #     if day < daysBack:
            #         cache[daysBack] = min(cache[daysBack-day] + costs[i], cache[daysBack])
            # print(cache)
            lastDay=day
        return cache[-1]
                
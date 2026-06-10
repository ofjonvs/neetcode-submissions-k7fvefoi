"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        from operator import attrgetter
        intervals.sort(key=attrgetter('start'))
        earliestEnds = [] 
        numRooms = 0
        for interval in intervals:
            if earliestEnds and interval.start >= earliestEnds[0]:
                heapq.heappop(earliestEnds)
                heapq.heappush(earliestEnds, interval.end)
            else:
                numRooms += 1
                heapq.heappush(earliestEnds, interval.end)
        return numRooms
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        from operator import attrgetter
        intervals.sort(key=attrgetter('start'))

        return not any(intervals[i].start < intervals[i-1].end for i in range(1, len(intervals)))
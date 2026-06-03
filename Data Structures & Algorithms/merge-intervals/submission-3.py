class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedIntervals = []
        curInterval = intervals[0]
        for start, end in intervals:
            if start <= curInterval[1]:
                curInterval[1] = max(end, curInterval[1])
            else:
                mergedIntervals.append(curInterval)
                curInterval = [start, end]
        return mergedIntervals + [curInterval]
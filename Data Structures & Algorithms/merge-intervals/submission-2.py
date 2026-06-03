class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedIntervals = []
        curInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= curInterval[1]:
                curInterval[1] = max(intervals[i][1], curInterval[1])
            else:
                mergedIntervals.append(curInterval)
                curInterval = intervals[i]
        return mergedIntervals + [curInterval]
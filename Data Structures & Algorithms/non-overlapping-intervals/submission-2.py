class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        numRemoved = 0
        curLeftInt = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[curLeftInt][1]:
                numRemoved += 1
                curLeftInt = i if intervals[i][1] < intervals[curLeftInt][1] else curLeftInt
            else:
                curLeftInt = i
        return numRemoved
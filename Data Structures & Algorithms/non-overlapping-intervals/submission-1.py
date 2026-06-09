class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        numRemoved = 0
        curLeftInt = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[curLeftInt][1]:
                numRemoved += 1
            else:
                curLeftInt = i
        return numRemoved
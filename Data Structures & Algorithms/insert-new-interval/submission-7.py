class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        newStart, newEnd = newInterval
        newIntvs = []
        for i, (start, end) in enumerate(intervals):
            if newStart < start:
                newIntvs.append([newStart])
                break
            if newStart <= end:
                newIntvs.append([start])
                break
            newIntvs.append([start, end])

        if len(newIntvs[-1]) == 2:
            return intervals + [newInterval]

        for j in range(i, len(intervals)):
            start, end = intervals[j]
            if newEnd < start:
                newIntvs[-1].append(newEnd)
                return newIntvs + intervals[j:]
            if newEnd <= end:
                newIntvs[-1].append(end)
                return newIntvs + intervals[j+1:]

        newIntvs[-1].append(newEnd)
        return newIntvs

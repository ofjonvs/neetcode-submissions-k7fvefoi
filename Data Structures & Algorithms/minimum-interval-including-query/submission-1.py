class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        from operator import itemgetter
        intervals.sort()
        queries = sorted(enumerate(queries), key=itemgetter(1))
        curInt = 0
        out = []
        heap = []
        for i, query in queries:
            while curInt < len(intervals) and intervals[curInt][0] <= query:
                heapq.heappush(heap, (intervals[curInt][1] - intervals[curInt][0] + 1, intervals[curInt][1]))
                curInt += 1
            
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            out.append((i, heap[0][0] if heap else -1))

        return [i[1] for i in sorted(out)]
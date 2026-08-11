class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = [(x[1], x[2], x[0]) for x in trips]
        heapq.heapify(heap)
        endHeap = []
        seats = 0
        while heap or endHeap:
            if not endHeap or (heap and endHeap[0][0] > heap[0][0]):
                trip = heapq.heappop(heap)
                heapq.heappush(endHeap, (trip[1], trip[0], trip[2]))
                seats += trip[2]
                if seats > capacity:
                    return False
            else:
                seats -= heapq.heappop(endHeap)[2]
        return True
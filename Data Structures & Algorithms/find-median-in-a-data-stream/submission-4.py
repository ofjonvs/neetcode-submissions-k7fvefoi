class MedianFinder:

    def __init__(self):
        import heapq
        class Heap:
            def __init__(self, min=True):
                self.heap = []
                self.size = 0
                self.min = min
            
            def insert(self, val):
                heapq.heappush(self.heap, val) if self.min else heapq.heappush_max(self.heap, val)
                self.size += 1
            
            def pop(self):
                self.size -= 1
                return heapq.heappop(self.heap) if self.min else heapq.heappop_max(self.heap)

            def peek(self):
                return self.heap[0]

        self.minHeap = Heap()
        self.maxHeap = Heap(False)

    def addNum(self, num: int) -> None:
        if self.minHeap.size and num > self.minHeap.peek():
            self.minHeap.insert(num)
            if self.minHeap.size - 1 > self.maxHeap.size:
                self.maxHeap.insert(self.minHeap.pop())
        else:
            self.maxHeap.insert(num)
            if self.maxHeap.size - 1 > self.minHeap.size:
                self.minHeap.insert(self.maxHeap.pop())
        

    def findMedian(self) -> float:
        if (self.maxHeap.size + self.minHeap.size)%2:
            return self.maxHeap.peek() if self.maxHeap.size > self.minHeap.size else self.minHeap.peek()
        return (self.minHeap.peek() + self.maxHeap.peek())/2
        
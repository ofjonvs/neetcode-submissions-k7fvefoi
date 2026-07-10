class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counts = Counter(tasks)
        heap = [(count, task) for task, count in counts.items()]
        heapq.heapify_max(heap)
        cycles = 0
        procQ = deque()
        while heap or procQ:
            while procQ and procQ[0][2] == cycles:
                count, task, _ = procQ.popleft()
                heapq.heappush_max(heap, (count, task))
            if heap:
                count, task = heapq.heappop_max(heap)
                (count - 1) and procQ.append((count-1, task, cycles+n+1))

            cycles += 1
        return cycles
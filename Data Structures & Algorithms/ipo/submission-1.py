class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq
        profitMaxHeap, capMinHeap = [], []
        for i in range(len(profits)):
            if capital[i] > w:
                heapq.heappush(capMinHeap, (capital[i], i))
            else:
                heapq.heappush_max(profitMaxHeap, (profits[i], i))

        for _ in range(k):
            if not profitMaxHeap:
                return w
            w += heapq.heappop_max(profitMaxHeap)[0]
            while capMinHeap and capMinHeap[0][0] <= w:
                idx = heapq.heappop(capMinHeap)[1]
                heapq.heappush_max(profitMaxHeap, (profits[idx], idx))
        return w
                    
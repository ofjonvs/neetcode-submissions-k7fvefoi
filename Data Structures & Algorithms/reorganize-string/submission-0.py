class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(cnt, c) for c, cnt in Counter(s).items()]
        heapq.heapify_max(heap)
        lastCnt, lastC = heapq.heappop_max(heap)
        out = lastC
        lastCnt -= 1
        while heap:
            cnt, c = heapq.heappop_max(heap)
            out += c
            lastCnt and heapq.heappush_max(heap, (lastCnt, lastC))
            lastCnt, lastC = cnt - 1, c
        return out if len(out) == len(s) else ''

        
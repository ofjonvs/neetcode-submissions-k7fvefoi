class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        from heapq import heapify, heappop, heappush
        heap = list(Counter(hand).items())
        heapify(heap)
        while heap:
            addBack = []
            for i in range(groupSize):
                if not heap:
                    return False
                addBack.append(heappop(heap))
                if len(addBack) > 1 and addBack[-1][0] != addBack[-2][0] + 1:
                    return False
            
            for card, count in addBack:
                (count - 1) and heappush(heap, (card, count-1))
        return True

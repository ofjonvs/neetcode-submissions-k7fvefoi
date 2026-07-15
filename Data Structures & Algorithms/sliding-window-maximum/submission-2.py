class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        if k >= len(nums):
            return [max(nums)]
        if k == 1:
            return nums
        
        heap = nums[:k]
        heapq.heapify_max(heap)
        garbage = defaultdict(int)
        res = []
        for i in range(k, len(nums)):
            while garbage.get(heap[0]):
                garbage[heapq.heappop_max(heap)] -= 1
            res.append(heap[0])
            garbage[nums[i-k]] += 1
            heapq.heappush_max(heap, nums[i])
        
        while garbage.get(heap[0]):
            garbage[heapq.heappop_max(heap)] -= 1
        return res + [heap[0]]

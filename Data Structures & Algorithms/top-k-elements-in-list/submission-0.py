class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda: 0)
        revCount = [set() for _ in range(len(nums)+1)]
        for num in nums:
            revCount[count[num]].discard(num)
            count[num] += 1
            revCount[count[num]].add(num)
        res, i = [], len(nums)-1
        while len(res) < k:
            res.extend(revCount[i])
            i -= 1
        return res
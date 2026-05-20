class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda: 0)
        for num in nums:
            count[num] += 1
        revCount = [[] for _ in range(len(nums)+1)]
        for num, cnt in count.items():
            revCount[cnt].append(num)
        res, i = [], len(nums)
        while len(res) != k:
            res.extend(revCount[i])
            i -= 1
        return res
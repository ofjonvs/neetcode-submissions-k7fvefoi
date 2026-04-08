class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = []
        curSum = 0
        hsh = defaultdict(lambda: 0)
        hsh[0] = 1
        res = 0
        for n in nums:
            curSum += n
            preSum.append(curSum)
            if curSum - k in hsh:
                res += hsh[curSum-k]
            hsh[curSum] += 1
        return res


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        from functools import cache

        @cache
        def rec(i, k):
            if k == 1:
                return sum(nums[i:])
            
            curSum = 0
            res = float('inf')
            for j in range(i, len(nums)-k+1):
                curSum += nums[j]
                res = min(res, max(curSum, rec(j+1, k-1)))
            return res

        return rec(0, k)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from functools import lru_cache

        @lru_cache(len(nums)*sum(abs(n) for n in nums))
        def recurse(i, curSum):
            if i >= len(nums):
                return int(curSum == target)
            return recurse(i+1, curSum+nums[i]) + recurse(i+1, curSum-nums[i])
        return recurse(0, 0)
            
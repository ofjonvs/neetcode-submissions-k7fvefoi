class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import cache

        nums = [1] + nums + [1]
        @cache
        def recurse(l, r):
            return max((nums[i]*nums[l]*nums[r] + recurse(l, i) + recurse(i, r) for i in range(l+1, r)), default=0)
        return recurse(0, len(nums)-1)
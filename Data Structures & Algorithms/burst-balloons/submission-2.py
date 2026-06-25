class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import cache

        nums = [1] + nums + [1]
        @cache
        def recurse(l, r):
            mul = nums[r]*nums[l]
            res = 0
            for i in range(l+1, r):
                res = max(res, nums[i]*mul + recurse(l, i) + recurse(i, r))
            return res
        return recurse(0, len(nums)-1)
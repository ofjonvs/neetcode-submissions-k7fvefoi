class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        @cache
        def helper(i, usedFirst):
            if i == len(nums)-1:
                return 0 if usedFirst else nums[i]
            if i >= len(nums):
                return 0
            return max(nums[i]+helper(i+2, usedFirst), helper(i+1, usedFirst))
        
        return max(nums[0]+helper(2, True), helper(1, False))
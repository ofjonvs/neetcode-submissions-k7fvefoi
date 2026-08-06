class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        from functools import cache

        @cache
        def rec(tot):
            if tot > target:
                return 0
            if tot == target:
                return 1
            
            return sum(rec(num + tot) for num in nums)

        return rec(0)

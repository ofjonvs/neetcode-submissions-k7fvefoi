class Solution:
    def canJump(self, nums: List[int]) -> bool:
        from functools import cache

        @cache
        def canJumpAtIdx(i):
            if i >= len(nums)-1:
                return True
            for j in range(nums[i], 0, -1):
                if canJumpAtIdx(i+j):
                    return True
            return False
        return canJumpAtIdx(0)
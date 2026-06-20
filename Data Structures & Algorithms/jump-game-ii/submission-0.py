class Solution:
    def jump(self, nums: List[int]) -> int:
        import functools

        @functools.cache
        def recurse(i):
            if i >= len(nums)-1:
                return 0
            if nums[i] == 0:
                return 100
            return 1 + min(recurse(j) for j in range(i+1, i+nums[i]+1))

        return recurse(0)
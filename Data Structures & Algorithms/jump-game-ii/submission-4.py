class Solution:
    def jump(self, nums: List[int]) -> int:
        def recurse(i):
            if i >= len(nums)-1:
                return 0
            if i + nums[i] >= len(nums)-1:
                return 1
            if nums[i] == 0:
                return 100
            maxStep = max((j for j in range(i+1, i+nums[i]+1)), key=lambda j: (j+nums[j], j))
            return 1 + recurse(maxStep)

        return recurse(0)
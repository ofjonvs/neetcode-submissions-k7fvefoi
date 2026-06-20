class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i, startSearch, jumps = 0, 1, 1
        while i + nums[i] < len(nums)-1:
            maxStep = max((j for j in range(startSearch, i+nums[i]+1)), key=lambda j: (j+nums[j], j))
            startSearch = i + nums[i]
            i = maxStep
            jumps += 1
        return jumps
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recurse(i, curSum):
            if i >= len(nums):
                return int(curSum == target)
            return recurse(i+1, curSum+nums[i]) + recurse(i+1, curSum-nums[i])
        return recurse(0, 0)
            
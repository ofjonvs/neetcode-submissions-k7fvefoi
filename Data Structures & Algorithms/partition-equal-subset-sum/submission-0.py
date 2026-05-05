class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (targSum:=sum(nums)) % 2 == 1:
            return False
        targSum //= 2

        from functools import lru_cache
        @lru_cache(len(nums)*targSum)
        def recurse(i, curSum):
            if i >= len(nums):
                return False
            if curSum == targSum:
                return True
            return recurse(i+1, curSum) or recurse(i+1, curSum+nums[i])
        return recurse(0, 0)
            

            
            
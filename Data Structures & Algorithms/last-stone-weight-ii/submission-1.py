class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        halfSum = sum(stones)/2

        from functools import lru_cache

        @lru_cache(len(stones)*int(halfSum))
        def recurse(i, curSum):
            if i >= len(stones):
                return abs(halfSum-curSum)
            return min(recurse(i+1, curSum), recurse(i+1, curSum+stones[i]))
        return math.ceil(recurse(0,0)*2)
class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt
        from functools import cache

        @cache
        def recurse(n):
            if not n:
                return 0
            sub = int(sqrt(n))
            minNum = n
            while sub > 1:
                minNum = min(minNum, 1 + recurse(n-sub**2))
                sub -= 1
            return minNum
        return recurse(n)
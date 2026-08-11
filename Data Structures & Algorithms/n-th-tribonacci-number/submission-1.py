class Solution:
    def tribonacci(self, n: int) -> int:
        from functools import cache

        @cache
        def trib(n):
            if n <= 2:
                return min(n, 1)
            return trib(n-1) + trib(n-2) + trib(n-3)
        return trib(n)
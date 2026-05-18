class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        from functools import lru_cache

        @lru_cache(len(s)*len(s))
        def rec(l, r):
            if l < 0 or r >= len(s):
                return 0
            if s[l] != s[r]:
                return max(rec(l-1, r), rec(l, r+1))
            return (1 if l == r else 2) + rec(l-1, r+1)

        return max(max(rec(i, i), rec(i, i+1)) for i in range(len(s)))
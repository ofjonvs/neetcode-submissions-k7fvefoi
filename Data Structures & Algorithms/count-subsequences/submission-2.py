class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        if len(t) > len(s):
            return 0
        
        @lru_cache(len(s)*len(t))
        def recurse(iS, iT):
            return 0 if iS == len(s) or iT == len(t) else \
            ((1 + recurse(iS+1, iT)) if iT == len(t) - 1 else \
            recurse(iS+1, iT+1) + recurse(iS+1, iT)) if s[iS] == t[iT] else \
            recurse(iS+1, iT)
        
        return recurse(0,0)

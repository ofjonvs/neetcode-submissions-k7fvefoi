class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = [1]+[0]*(len(t))
        for iS, cs in enumerate(s):
            newCache = cache.copy()
            for iT in range(1, len(t)+1):
                if t[iT-1] == cs:
                    newCache[iT] += cache[iT-1]
            cache = newCache

        return cache[-1]
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import lru_cache

        @lru_cache(len(word1)*len(word2))
        def helper(i1, i2):
            if i1 == len(word1):
                return len(word2) - i2
            if i2 == len(word2):
                return len(word1) - i1
            if word1[i1] != word2[i2]:
                return 1 + min(helper(i1+1, i2), helper(i1, i2+1), helper(i1+1, i2+1))
            return helper(i1+1, i2+1)
        
        return helper(0, 0)
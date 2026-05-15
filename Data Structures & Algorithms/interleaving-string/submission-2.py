class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        from functools import lru_cache
        @lru_cache(len(s1)*len(s2))
        def rec(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return True
            if i1 == len(s1):
                return rec(i1, i2+1) if s2[i2] == s3[i1+i2] else False
            if i2 == len(s2):
                return rec(i1+1, i2) if s1[i1] == s3[i1+i2] else False
            
            if (s3[i1+i2], s3[i1+i2]) == (s1[i1], s2[i2]):
                return rec(i1+1, i2) or rec(i1, i2+1)
            elif s3[i1+i2] == s1[i1]:
                return rec(i1+1, i2)
            elif s3[i1+i2] == s2[i2]:
                return rec(i1, i2+1)
            else:
                return False
        return rec(0, 0)
            
            
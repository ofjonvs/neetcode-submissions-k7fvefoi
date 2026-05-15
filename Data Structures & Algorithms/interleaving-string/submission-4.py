class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s2) < len(s1):
            s2, s1 = s1, s2
    
        cache = [True] + [c1 == c3 for c1, c3 in zip(s1, s3)]
        for i2, c2 in enumerate(s2):
            cache[0] = cache[0] and c2 == s3[i2]
            for i1, c1 in enumerate(s1):
                cache[i1+1] = cache[i1] if c1 == s3[i1+i2+1] else cache[i1+1] if c2 == s3[i1+i2+1] else False

        return cache[-1]


        
        
            
            
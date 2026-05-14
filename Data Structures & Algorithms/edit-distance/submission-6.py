class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = list(range(len(word1)+1))
        for i2, c1 in enumerate(word2):
            cache2 = cache.copy()
            cache2[0] = i2+1
            for i in range(1, len(word1)+1):
                if word1[i-1] == c1:
                    cache2[i] = cache[i-1]
                else:
                    cache2[i] = 1 + min(cache2[i-1], cache[i], cache[i-1])
            cache = cache2
            
        return cache[-1]

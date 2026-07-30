class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        # word1, word2 = (word1, word2) if len(word1) > len(word2) else (word2, word1)
        for i, (c1, c2) in enumerate(zip(word1, word2)):
            s += c1 + c2
        return s + word1[i+1:] + word2[i+1:]
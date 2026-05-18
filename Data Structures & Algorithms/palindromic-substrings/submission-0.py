class Solution:
    def countSubstrings(self, s: str) -> int:
        numPals = 0
        for i in range(len(s)):
            for l, r in ((i, i), (i, i+1)):
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        numPals += 1
                    else:
                        break
                    l -= 1
                    r += 1
        return numPals
            
        
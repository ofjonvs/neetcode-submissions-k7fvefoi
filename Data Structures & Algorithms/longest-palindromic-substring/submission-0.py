class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal = -1
        for i in range(len(s)):
            for l, r in ((i, i), (i, i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r-l-2 > maxPal:
                    lRange, rRange = l+1, r
                    maxPal = r-l-2
        
        return s[lRange:rRange]
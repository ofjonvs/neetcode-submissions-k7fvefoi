class Solution:
    def numDecodings(self, s: str) -> int:
        numDec = 0
        oneBack = 1
        twoBack = 1
        for i in range(len(s)):
            if s[i] != '0':
                numDec = oneBack
            if i > 0 and (s[i-1] == '1' or (int(s[i]) <= 6 and s[i-1] == '2')):
                numDec += twoBack

           
            twoBack, oneBack, numDec = oneBack, numDec, 0
        return oneBack
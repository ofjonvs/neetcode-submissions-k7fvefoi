class Solution:
    def numDecodings(self, s: str) -> int:
        numDec = 0
        oneBack = 1
        twoBack = 1
        for i in range(len(s)):
            numDec = 0
            if s[i] != '0':
                numDec = oneBack
            if i > 0 and (s[i-1] == '1' or (int(s[i]) <= 6 and s[i-1] == '2')):
                numDec += twoBack

            if numDec == 0:
                return 0
            twoBack, oneBack = oneBack, numDec
        return oneBack
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ''
        getChar = lambda x: chr(x+64)
        while columnNumber:
            out += getChar((columnNumber-1)%26+1)
            columnNumber -= 1
            columnNumber //= 26
        return out[::-1]
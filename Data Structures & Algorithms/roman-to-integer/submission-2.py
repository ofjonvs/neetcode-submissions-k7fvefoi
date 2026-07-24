class Solution:
    def romanToInt(self, s: str) -> int:
        symbMap = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000,
        }
        out = i = 0
        while i < len(s) - 1:
            c, nc = s[i], s[i+1]
            if (c == 'I' and nc in 'VX') or \
                (c == 'X' and nc in 'LC') or \
                (c == 'C' and nc in 'DM'):
                out += symbMap[nc] - symbMap[c]
                i += 2
            else:
                out += symbMap[c]
                i += 1
    
        return out + (symbMap[s[i]] if i == len(s)-1 else 0)
            

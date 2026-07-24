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
            match s[i]:
                case 'I' if s[i+1] in 'VX':
                    out += symbMap[s[i+1]] - 1
                    i += 2
                case 'X' if s[i+1] in 'LC':
                    out += symbMap[s[i+1]] - 10
                    i += 2
                case 'C' if s[i+1] in 'DM':
                    out += symbMap[s[i+1]] - 100
                    i += 2
                case _:
                    out += symbMap[s[i]]
                    i += 1
        return out + (symbMap[s[i]] if i == len(s)-1 else 0)
            

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def getDivs(s):
            divs = {s}
            for i in range(1, len(s)//2 + 1):
                if len(s) % i:
                    continue
                sub = s[:i]
                isDiv = True
                
                for j in range(i, len(s), i):
                    if sub != s[j:j+i]:
                        isDiv = False
                        break
                if isDiv:
                    divs.add(sub)
            return divs

        return max(getDivs(str1)&getDivs(str2), key=lambda x: len(x), default='')
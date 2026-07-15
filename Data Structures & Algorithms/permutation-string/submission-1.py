class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ct = Counter(s1)
        curCt = {}
        numMatched = 0
        l = 0
        for i, c in enumerate(s2):
            if c not in ct:
                curCt = {}
                numMatched = 0
                l = i+1
            else:
                curCt[c] = curCt.get(c, 0) + 1
                if curCt[c] == ct[c]:
                    numMatched += 1
                
                while curCt[c] > ct[c]:
                    char_l = s2[l]
                    if curCt[char_l] == ct[char_l]:
                        numMatched -= 1
                    curCt[char_l] -= 1
                    l += 1
                
                if numMatched == len(ct):
                    return True

        return False

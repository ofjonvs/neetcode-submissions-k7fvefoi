class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        l = r = 0
        minLen = float('inf')
        minL = minR = None
        numValChars = 0
        if s[0] in cnt:
            cnt[s[0]] -= 1
            if cnt[s[r]] == 0:
                numValChars += 1
        while l < len(s):
            if numValChars != len(cnt):
                r += 1
                if r == len(s):
                    break
                if s[r] in cnt:
                    cnt[s[r]] -= 1
                    if cnt[s[r]] == 0:
                        numValChars += 1
            else: # valid substring
                if r-l < minLen:
                    minL, minR = l, r+1
                    minLen = r-l
                if s[l] in cnt:
                    cnt[s[l]] += 1
                    if cnt[s[l]] > 0:
                        numValChars -= 1
                l += 1
        return s[minL:minR] if minL is not None else ''
                
                    
                
            
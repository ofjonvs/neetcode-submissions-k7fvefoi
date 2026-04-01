class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = {}
        l = res = curr = 0
        for r, c in enumerate(s):
            if c in dup:
                newL = dup[c] + 1
                for i in range(l, newL):
                    dup.pop(s[i], None)
                l = newL
                curr = r - l + 1
                dup[c] = r
            else:
                dup[c] = r
                curr += 1
                res = max(curr, res)
        return res

                
        
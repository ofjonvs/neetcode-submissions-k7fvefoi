class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(lambda:0)
        maxCount = l = res = 0
        for r, c in enumerate(s):
            strLen = r - l + 1
            count[c] += 1
            maxCount = max(maxCount, count[c])
            if strLen - maxCount <= k:
                res = max(res, strLen)
            else:
                if count[s[l]] == maxCount:
                    maxCount -= 1
                count[s[l]] -= 1
                l += 1

        return res

        
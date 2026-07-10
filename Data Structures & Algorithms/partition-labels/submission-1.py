class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = {}
        for i, c in enumerate(s):
            indices[c] = i
        i = 0
        res = []
        while i < len(s):
            start = i
            lastIdx = indices[s[i]]
            j = i
            while j <= lastIdx:
                lastIdx = max(indices[s[j]], lastIdx)
                j += 1
            res.append(lastIdx - start + 1)
            i = lastIdx + 1
        return res
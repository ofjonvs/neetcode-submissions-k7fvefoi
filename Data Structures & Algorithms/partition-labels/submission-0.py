class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = {}
        for i, c in enumerate(s):
            indices.setdefault(c, []).append(i)
        i = 0
        res = []
        while i < len(s):
            start = i
            lastIdx = indices[s[i]][-1]
            j = i
            while j <= lastIdx:
                lastIdx = max(indices[s[j]][-1], lastIdx)
                j += 1
            res.append(lastIdx - start + 1)
            i = lastIdx + 1
        return res
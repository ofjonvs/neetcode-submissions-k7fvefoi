class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # aInRow = bInRow = cInRow = 0
        inRow = {ch: 0 for ch in 'abc'}
        numChs = {ch: v for ch, v in zip('abc', (a, b, c)) if v}
        out = ''
        while inRow and numChs:
            print(inRow, numChs)
            maxCh, _ = max(((ch, v) for ch, v in numChs.items() if ch in inRow), key=lambda x: x[1], default=(None, None))
            if maxCh is None:
                return out
            out += maxCh
            if inRow[maxCh] == 1:
                inRow.pop(maxCh)
            else:
                inRow = {ch: 0 for ch in 'abc'}
                inRow[maxCh] = 1
            numChs[maxCh] -= 1
            not numChs[maxCh] and numChs.pop(maxCh)
            
        return out
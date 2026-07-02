class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 1 2 4
        if not (vals := self.table[key]) or timestamp < vals[0][0]:
            return ''
        if timestamp >= vals[-1][0]:
            return vals[-1][1]
        l, r = 0, len(vals)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
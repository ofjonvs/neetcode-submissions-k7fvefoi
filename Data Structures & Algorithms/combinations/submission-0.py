class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # n!/(n-k)!k!
        res = []
        def recurse(lst, i):
            if len(lst) == k:
                res.append(lst.copy())
                return
            if i <= n:
                lst.append(i)
                recurse(lst, i+1)
                lst.pop()

                recurse(lst, i+1)

        for i in range(1, n+1):
            recurse([i], i+1)
        return res
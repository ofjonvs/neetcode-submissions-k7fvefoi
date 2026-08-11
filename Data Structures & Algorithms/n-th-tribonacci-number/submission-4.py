class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        trib = [0, 1, 1]
        for i in range(3, n+1):
            trib = trib[1], trib[2], sum(trib)
        return trib[-1]
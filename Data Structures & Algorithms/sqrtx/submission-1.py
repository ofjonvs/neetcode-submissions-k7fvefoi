class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            sq = i*i
            if sq == x:
                return i
            elif sq > x:
                return i - 1
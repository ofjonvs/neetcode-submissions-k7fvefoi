class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        base, i = x, 1
        while i < abs(n)/2:
            x *= x
            i *= 2
        
        for j in range(i, abs(n)):
            x *= base
        return x if n >= 0 else 1/x
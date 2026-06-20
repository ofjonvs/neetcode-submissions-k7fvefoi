class Solution:
    def myPow(self, x: float, n: int) -> float:
        base, x = x if n > 0 else 1/x, 1
        for _ in range(abs(n)):
            x *= base
        return x
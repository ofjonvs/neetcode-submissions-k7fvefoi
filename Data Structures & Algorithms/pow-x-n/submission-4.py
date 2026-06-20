class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if not n:
                return 1
            if not x:
                return 0
            
            res = pow(x*x, n//2)
            return x * res if n % 2 else res
        res = pow(x, abs(n))
        return res if n > 0 else 1/res
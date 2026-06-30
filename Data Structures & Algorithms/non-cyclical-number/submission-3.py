class Solution:
    def isHappy(self, n: int) -> bool:
        nBy2 = n
        while True:
            n = sum(int(dig)**2 for dig in str(n))
            nBy2 = sum(int(dig)**2 for dig in str(sum(int(dig)**2 for dig in str(nBy2))))
            if n == 1:
                return True
            elif n == nBy2:
                return False
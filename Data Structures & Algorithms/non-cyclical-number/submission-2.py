class Solution:
    def isHappy(self, n: int) -> bool:
        set_ = {n}
        while True:
            n = sum(int(dig)**2 for dig in str(n))
            if n == 1:
                return True
            elif n in set_:
                return False
            set_.add(n)
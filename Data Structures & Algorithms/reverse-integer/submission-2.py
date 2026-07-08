class Solution:
    def reverse(self, x: int) -> int:
        LOW, HIGH = -2**31, 2**31-1
        res = 0
        while x:
            dig = int(math.fmod(x, 10))
            x = int(x/10)
            if res > HIGH // 10 or (res == HIGH // 10 and dig >= HIGH % 10) \
                or res < LOW // 10 or (res == LOW // 10 and dig <= LOW % 10):
                return 0
            res = res*10 + dig
        return res


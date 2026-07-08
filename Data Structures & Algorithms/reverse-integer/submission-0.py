class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = int('-' + x[1:][::-1])
        else:
            x = int(x[::-1])
        if -2**31 <= x <= 2**31-1:
            return x
        return 0
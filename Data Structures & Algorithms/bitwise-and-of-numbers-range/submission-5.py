class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        incs = 0
        while left != right:
            left >>= 1
            right >>= 1
            incs += 1
        return left << incs

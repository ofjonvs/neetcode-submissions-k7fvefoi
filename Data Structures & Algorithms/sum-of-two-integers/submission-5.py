class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for i in range(32):
            aBit, bBit = (a >> i) & 1, (b >> i) & 1
            curBit = 1 if (aBit and not bBit and not carry) or (not aBit and bBit and not carry) or (not aBit and not bBit and carry) or (aBit and bBit and carry) else 0
            res = res | curBit << i
            carry = 1 if (aBit and bBit) or (aBit and carry) or (bBit and carry) else 0
        return res if res < (1 << 31) else ~(res ^ 0xFFFFFFFF)

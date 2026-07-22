class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1], carry = (0, 1) if digits[-1] == 9 else (digits[-1]+1, 0)
        for i in range(len(digits)-2, -1, -1):
            digits[i], carry = (0, 1) if digits[i]+carry == 10 else (digits[i]+carry, 0)
        return carry and [1]+digits or digits
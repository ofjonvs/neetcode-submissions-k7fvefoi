class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct, numZeros = 1, 0
        for num in nums:
            if num:
                totalProduct *= num
            else:
                numZeros += 1
        return [0 if numZeros > 1 or numZeros == 1 and num != 0 else totalProduct//num if num else totalProduct for num in nums]
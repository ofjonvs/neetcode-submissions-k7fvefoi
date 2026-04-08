class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = nums.copy(), nums.copy()
        for i in range(1, len(nums)):
            prefix[i] *= prefix[i-1]
            postfix[-i-1] *= postfix[-i] 
        return [postfix[1]] + [prefix[i-1]*postfix[i+1] for i in range(1, len(nums)-1)] + [prefix[-2]]
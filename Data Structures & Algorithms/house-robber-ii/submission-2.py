class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        maxIncLast = maxNotIncLast = 0
        for i in range(1, len(nums)):
            maxIncLast, maxNotIncLast = nums[i] + maxNotIncLast, max(maxIncLast, maxNotIncLast)
        firstIterMax = max(maxIncLast, maxNotIncLast)

        maxIncLast = maxNotIncLast = 0
        for i in range(len(nums)-1):
            maxIncLast, maxNotIncLast = nums[i] + maxNotIncLast, max(maxIncLast, maxNotIncLast)
        
        return max(firstIterMax, maxIncLast, maxNotIncLast)

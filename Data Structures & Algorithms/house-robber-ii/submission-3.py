class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob = nums[0]
        for start, end in (1, len(nums)), (0, len(nums)-1):
            maxIncLast = maxNotIncLast = 0
            for i in range(start, end):
                maxIncLast, maxNotIncLast = nums[i] + maxNotIncLast, max(maxIncLast, maxNotIncLast)
            maxRob = max(maxRob, maxIncLast, maxNotIncLast)
        
        return maxRob

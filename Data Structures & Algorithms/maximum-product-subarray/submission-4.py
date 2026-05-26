class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curMax = 0
        curMinThread = curMaxThread = 1
        for num in nums:
            curMaxThreadTmp = curMaxThread
            curMaxThread = max(num, curMaxThread*num, curMinThread*num)
            curMinThread = min(num, curMinThread*num, curMaxThreadTmp*num)
            curMax = max(curMax, curMaxThread, curMinThread)
        return curMax


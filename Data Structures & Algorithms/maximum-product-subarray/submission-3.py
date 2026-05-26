class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curMax = 0
        for _ in range(2):
            curMinThread = curMaxThread = 1
            for num in nums:
                if num < 0:
                    if curMinThread < 0:
                        curMinThread *= num
                        curMaxThread = curMinThread
                        curMax = max(curMinThread, curMax)
                    else:
                        curMaxThread = 1
                        curMinThread *= num
                elif num == 0:
                    curMinThread = curMaxThread = 1
                else:
                    curMinThread *= num
                    curMaxThread *= num
                    curMax = max(curMax, curMaxThread, curMinThread)
            nums.reverse()
        return curMax


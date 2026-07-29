class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = lMax = 0
        curMax = 1
        for r in range(1, len(nums)):
            if nums[r] == nums[r-1]:
                curMax += 1
            else:
                if curMax > lMax and nums[r] != nums[l]:    
                    l, lMax = r-1, curMax
                curMax = 1
        return nums[l] if lMax > curMax else nums[-1]
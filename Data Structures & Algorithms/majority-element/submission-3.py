class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = curMax = 0
        for num in nums:
            if curMax == 0:
                res = num
            curMax += 1 if res == num else -1
        return res
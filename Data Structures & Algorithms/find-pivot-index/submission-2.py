class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        if 0 == nums[-1]-nums[0]:
            return 0
        # elif len(nums) > 1 and nums[-2] == 0:
        #     return len(nums)-1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[-1] - nums[i]:
                return i
        return -1
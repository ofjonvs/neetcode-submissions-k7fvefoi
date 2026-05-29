class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(None)
        cur = nums[0]
        for i in range(len(nums)-1):
            while i != nums[i] and nums[i] is not None:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return nums.index(None)


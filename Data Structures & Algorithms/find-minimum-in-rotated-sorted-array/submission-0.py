class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums)-1
        while l < r:
            mid = (r - l + 2*l)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [nums[0]]
        for i in range(1, len(nums)):
            self.nums.append(self.nums[i-1]+nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - (left and self.nums[left-1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
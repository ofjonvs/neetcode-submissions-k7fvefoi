class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = nums[0], nums[nums[0]]
        while s != f:
            s, f = nums[s], nums[nums[f]]
        s2 = 0
        while s!=s2:
            s, s2 = nums[s], nums[s2]
        return s
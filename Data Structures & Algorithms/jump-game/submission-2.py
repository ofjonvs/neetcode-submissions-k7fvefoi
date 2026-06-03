class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curJump = 1
        for i in range(len(nums)):
            if not curJump:
                return False
            curJump -= 1
            curJump = max(curJump, nums[i])
        return True
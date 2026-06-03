class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curJump = 1
        for num in nums:
            if not curJump:
                return False
            curJump = max(curJump-1, num)
        return True
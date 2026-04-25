class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(idxs, perm):
            if len(idxs) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if i in idxs:
                    continue
                perm.append(nums[i])
                idxs.add(i)
                recurse(idxs, perm)
                idxs.remove(i)
                perm.pop()
        recurse(set(), [])
        return res
                
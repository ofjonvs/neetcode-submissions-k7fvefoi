class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i, tg):
            hsh = {}
            res = []
            for j in range(i+1, len(nums)):
                if (i1:=(tg - nums[j])) in hsh:
                    res.extend([(nums[j], i1) for _ in range(hsh[i1])])
                hsh[nums[j]] = hsh.get(nums[j], 0) + 1
            return res
        res = set()
        for i in range(len(nums)):
            for twoSumRes in twoSum(i, -nums[i]):
                res.add(tuple(sorted((nums[i], *twoSumRes))))
        return [list(t) for t in res]
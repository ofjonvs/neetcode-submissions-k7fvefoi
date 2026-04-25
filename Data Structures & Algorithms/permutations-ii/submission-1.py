class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(idxs, perm, permSet):
            if len(idxs) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if i in idxs or permSet[nums[i]][-1] < i:
                    continue
                perm.append(nums[i])
                permSet[nums[i]].append(i)
                idxs.add(i)
                recurse(idxs, perm, permSet)
                idxs.remove(i)
                permSet[perm.pop()].pop()
        recurse(set(), [], defaultdict(lambda: [float('inf')]))
        return res
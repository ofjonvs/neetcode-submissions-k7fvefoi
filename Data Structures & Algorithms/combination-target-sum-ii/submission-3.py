class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        def recurse(i, path, curSum):
            if curSum == target:
                out.append(path.copy())
                return
            if i >= len(candidates) or curSum > target:
                return
            
            path.append(candidates[i])
            recurse(i+1, path, curSum+candidates[i])
            path.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            recurse(i + 1, path, curSum)

        recurse(0, [], 0)
        return out
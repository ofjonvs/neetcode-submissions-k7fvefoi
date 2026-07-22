class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = set()
        def recurse(i, path, curSum):
            if curSum == target:
                out.add(tuple(path))
                return
            if curSum > target:
                return
            
            for j in range(i+1, len(candidates)):
                if j > i + 1 and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                recurse(j, path, curSum+candidates[j])
                path.pop()
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            recurse(i, [candidates[i]], candidates[i])
        return [list(i) for i in out]
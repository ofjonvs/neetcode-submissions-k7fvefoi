class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out, path, curSum = [], [], 0
        def recurse(i):
            nonlocal curSum
            if curSum == target:
                out.append(path.copy())
                return
            if i >= len(candidates) or curSum > target:
                return
            
            path.append(candidates[i])
            tmp = curSum
            curSum += candidates[i]
            recurse(i+1)
            path.pop()
            curSum = tmp
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            recurse(i+1)

        recurse(0)
        return out
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache(len(strs)*m*n)
        def recurse(i, curM, curN):
            if curM > m or curN > n:
                return -len(strs)
            if i >= len(strs):
                return 0
            return max(1+recurse(i+1, curM+strs[i].count('0'), curN+strs[i].count('1')), recurse(i+1,curM, curN))
        return recurse(0, 0, 0)

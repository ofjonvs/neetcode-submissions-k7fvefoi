class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        from functools import cache
        @cache
        def branch(i):
            if i == len(s):
                return 0
            res = 1 + branch(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    res = min(res, branch(j+1))
            return res

        return branch(0)
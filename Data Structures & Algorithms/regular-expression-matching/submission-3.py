class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import functools
        isEqual = lambda i, j: i < len(s) and (s[i] == p[j] or p[j] == '.')

        @functools.cache
        def helper(i, j):
            if j == len(p):
                return i == len(s)
            if j < len(p) - 1 and p[j+1] == '*':
                return helper(i, j+2) or (isEqual(i, j) and helper(i+1, j))
            elif isEqual(i, j):
                return helper(i+1, j+1)
            return False
        return helper(0, 0)
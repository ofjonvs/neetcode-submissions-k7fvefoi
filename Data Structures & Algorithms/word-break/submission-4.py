class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import cache

        @cache
        def recurse(i):
            if i == len(s):
                return True
            if i > len(s):
                return False
            
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if recurse(i+len(word)):
                        return True
            return False

        return recurse(0)

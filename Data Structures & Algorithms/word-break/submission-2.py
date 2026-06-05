class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import cache

        @cache
        def recurse(i, word):
            if i == len(s):
                return True
            if i > len(s):
                return False
            
            if s[i:i+len(word)] == word:
                return any(recurse(i+len(word), newWord) for newWord in wordDict)
            return False

        return any(recurse(0, word) for word in wordDict)

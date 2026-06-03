class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import cache

        @cache
        def helper(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            return helper(i+1) + (helper(i+2) if i < len(s)-1 and (s[i] == '1' or s[i] == '2' and int(s[i+1]) <= 6) else 0)
            
        return helper(0)
        
            


        
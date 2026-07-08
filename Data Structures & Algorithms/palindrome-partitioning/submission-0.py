class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s2):
            start, end = 0, len(s2)-1
            while end - start > 0:
                if s2[start] != s2[end]:
                    return False
                start += 1
                end -= 1
            return True

        res = []
        pals = []
        def recurse(i):
            if i >= len(s):
                res.append(pals.copy())
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    pals.append(s[i:j+1])
                    recurse(j+1)
                    pals.pop()
        recurse(0)
        return res        
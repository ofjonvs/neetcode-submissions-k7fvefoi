class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        chars = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno',
        'pqrs', 'tuv', 'wxyz']

        res = list(chars[int(digits[0])])
        for i in range(1, len(digits)):
            res = [s+c for s in res for c in chars[int(digits[i])]]
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = ''
        def recurse(L, R):
            nonlocal s
            sTemp = s
            if not L:
                res.append(s+')'*R)
            elif L == R:
                s += '('
                recurse(L-1, R)
                s = sTemp
            else:
                s += '('
                recurse(L-1, R)
                s = sTemp
                s += ')'
                recurse(L, R-1)
                s = sTemp
        recurse(n, n)   
        return res    

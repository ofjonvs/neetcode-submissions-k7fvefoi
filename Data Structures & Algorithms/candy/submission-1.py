class Solution:
    def candy(self, ratings: List[int]) -> int:
        from itertools import pairwise
        gaus = lambda n: n*(n+1)//2
        out = 0
        inc = dec = 0
        for kid1, kid2 in pairwise(ratings):
            if kid2 < kid1:
                dec += 1
            elif kid2 > kid1:
                if dec:
                    out += gaus(max(inc, dec) + 1) + gaus(min(inc, dec)) - 1
                    inc = dec = 0
                inc += 1
            else:
                out += gaus(max(inc, dec) + 1) + gaus(min(inc, dec))
                inc = dec = 0
        
        return out + gaus(max(inc, dec) + 1) + gaus(min(inc, dec))
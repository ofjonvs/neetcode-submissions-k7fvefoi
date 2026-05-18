class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [list(range(len(str2)+1)) for _ in range(len(str1)+1)]
        for i1 in range(1, len(str1)+1):
            dp[i1][0] = dp[i1-1][0] + 1
            for i2 in range(1, len(str2)+1):
                dp[i1][i2] = 1 + dp[i1-1][i2-1] if str1[i1-1] == str2[i2-1] else 1 + min(dp[i1][i2-1], dp[i1-1][i2])
        
        comsub = []
        i1, i2 = len(str1), len(str2)
        while i1 and i2:
            if str1[i1-1] == str2[i2-1]:
                comsub.append(str1[i1-1])
                i1 -= 1
                i2 -= 1
            elif dp[i1-1][i2] < dp[i1][i2-1]:
                i1 -= 1
                comsub.append(str1[i1])
            else:
                i2 -= 1
                comsub.append(str2[i2])
        
        while i1:
            i1 -= 1
            comsub.append(str1[i1])
        while i2:
            i2 -= 1
            comsub.append(str2[i2])
        return ''.join(comsub[::-1])
        


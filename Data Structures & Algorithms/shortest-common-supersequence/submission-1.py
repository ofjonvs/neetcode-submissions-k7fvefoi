class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
          a     b      a       c
        c ac    abc    abca    abca
        a ca    cab    abca    abcac
        b cab   cab    caba    cabac
        """
        str1, str2 = str2, str1
        dp = ['']+[str2[:i+1] for i in range(len(str2))]
        for i1 in range(len(str1)):
            dpNew = [dp[0]+str1[i1]]
            for i2 in range(1, len(str2)+1):
                if str1[i1] == str2[i2-1]:
                    dpNew.append(dp[i2-1] + str1[i1])
                else:
                    if len(dp[i2]) < len(dpNew[i2-1]):
                        dpNew.append(dp[i2] + str1[i1])
                    else:
                        dpNew.append(dpNew[i2-1] + str2[i2-1])
            dp = dpNew
        return dp[-1]
        


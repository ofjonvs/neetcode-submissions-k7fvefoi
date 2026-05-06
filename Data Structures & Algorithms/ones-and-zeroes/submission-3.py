class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            num0s, num1s = s.count('0'), s.count('1')
            newDp = [[0]*(n+1) for _ in range(m+1)]
            for i in range(m+1):
                for j in range(n+1):
                    if num0s <= i and num1s <= j: 
                        newDp[i][j] = max(1 + dp[i-num0s][j-num1s], dp[i][j])
                    else:
                        newDp[i][j] = dp[i][j]

            dp = newDp
        return dp[m][n]

